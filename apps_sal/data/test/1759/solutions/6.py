(n, m) = map(int, input().split())
t = [0 for i in range(m)]
for i in range(n):
    c = list(map(int, input().split()))
    t[0] += c[0]
    for j in range(1, m):
        t[j] = max(t[j], t[j - 1]) + c[j]
    print(t[m - 1], end=' ')
