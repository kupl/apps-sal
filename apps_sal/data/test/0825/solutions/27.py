def div(n):
    i = 2
    a = n
    D = {}
    tmp = 1
    while i * i <= n:
        cnt = 0
        while a % i == 0:
            a = a // i
            tmp *= i
            cnt += 1
        if cnt > 0:
            D[i] = cnt
        i += 1
    if tmp != n:
        D[n] = 1
    return D


N = int(input())
D = div(N)
ans = 0
for v in D.values():
    i = 1
    total = 1
    while v >= total + (i + 1):
        i += 1
        total += i
    ans += i

print(ans)
