from math import ceil
n, h = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
max_a = max([lst[i][0] for i in range(n)])
b = sorted(lst[i][1] for i in range(n)) + [0]
for i in range(n - 1, -1, -1):
    b[i] += b[i + 1]
ans = 10**10
for i in range(n + 1):
    hp = h - b[i]
    t = max(0, ceil(hp / max_a))
    t += n - i
    ans = min(ans, t)
print(ans)
