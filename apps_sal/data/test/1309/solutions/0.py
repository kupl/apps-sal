n = int(input())
x = list(map(int, input().split()))

x.sort()

mn = 10**10
for a in range(2 * n):
    for b in range(a + 1, 2 * n):
        p = x[:a] + x[a + 1:b] + x[b + 1:]
        sm = 0
        for i in range(n - 1):
            sm += p[2 * i + 1] - p[2 * i]
        mn = min(mn, sm)

print(mn)
