def erat(n):
    n += 1
    l = [1 for _ in range(n)]
    (l[0], l[1]) = (0, 0)
    for i in range(4, n, 2):
        l[i] = 0
    for i in range(9, n, 6):
        l[i] = 0
    for i in range(6, n, 6):
        if l[i - 1]:
            for j in range((i - 1) * (i - 1), n, i - 1):
                l[j] = 0
        if l[i + 1]:
            for j in range((i + 1) * (i + 1), n, i + 1):
                l[j] = 0
    return l


prime = []
for i in range(1001):
    if erat(1000)[i]:
        prime.append(i)
n = int(input())
u = [0] * 1001
for i in range(1, n + 1):
    for j in prime:
        while i % j == 0:
            i //= j
            u[j] += 1
ans = 1
for i in u:
    ans *= i + 1
print(ans % (10 ** 9 + 7))
