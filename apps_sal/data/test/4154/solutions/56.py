n, m = list(map(int, input().split()))
ans = [i for i in range(1, n + 1)]

l_max = 0
r_min = n

for _ in range(m):
    x, y = list(map(int, input().split()))
    l_max = max(l_max, x)
    r_min = min(r_min, y)

print((len([i for i in range(l_max, r_min + 1)])))

