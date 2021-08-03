N = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
a = max(A)
prime_num = [2]
sgn = [0 for _ in range(max(int(a**0.5) + 1, 4))]
sgn[2] = 1
for k in range(3, len(sgn), 2):
    if sgn[k] == 0:
        prime_num.append(k)
        for j in range(k, a + 1, k**2):
            sgn[k] = 1
baisu = []
count = [0 for _ in range(a + 1)]
for k in range(N):
    b = 0 + A[k]
    for p in prime_num:
        if p**2 <= b:
            if b % p == 0:
                if count[p] == 0:
                    baisu.append(p)
                c = 0
                while b % p == 0:
                    b //= p
                    c += 1
                if c > count[p]:
                    count[p] = c
        else:
            break
    if b != 1:
        if count[b] == 0:
            count[b] = 1
            baisu.append(b)

product = 1
for item in baisu:
    product *= pow(item, count[item], mod)
    product %= mod

b = mod - 2
blis = []
c = 0
while b > 0:
    if b & 1 == 1:
        blis.append(c)
    c += 1
    b >>= 1


def modinv(a):
    if a == 1:
        return 1
    else:
        res = 1
        li = []
        for _ in range(c):
            li.append(a % mod)
            a = a * a % mod
        for item in blis:
            res = res * li[item] % mod
        return res


ans = 0
for k in range(N):
    ans += product * modinv(A[k])
    ans %= mod

print(ans)
