def prime_factorize(n):
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            arr.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        arr.append(n)
    return arr


from collections import Counter

n = int(input())
c = Counter(prime_factorize(n))
cnt = 0
for k, v in list(c.items()):
    if v == 1:
        cnt += 1
    else:
        v0 = 1
        while v-v0 >= 0:
            v -= v0
            cnt += 1
            v0 += 1

print(cnt)

