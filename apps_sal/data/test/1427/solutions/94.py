n = int(input())
a = list(map(int, input().split()))
so_list = [0 for i in range(10**6)]
mod = 10**9 + 7


def fac(n):
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            if so_list[i] < cnt:
                so_list[i] = cnt
    if temp != 1:
        #  print(temp)
        if so_list[temp] == 0:
            so_list[temp] = 1


for i in range(n):
    a1 = a[i]
    fac(a1)
l = 1
for i in range(len(so_list)):
    if so_list[i] != 0:
        l *= pow(i, so_list[i], mod)
        l %= mod
ans = 0
# print(l)
for i in a:
    t = pow(i, mod - 2, mod)
    ans += (l * t) % mod
print((ans % mod))
