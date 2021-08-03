n, a, b = list(map(int, input().split()))
l = []
c = 0
k = 0

for i in range(n + 1):
    k = i
    c = 0
    while (i > 0):
        c += i % 10
        i //= 10
    if (a <= c <= b):
        l.append(k)

print((sum(l)))
