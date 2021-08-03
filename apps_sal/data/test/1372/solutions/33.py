h, n = map(int, input().split())
c = [list(map(int, input().split()))for _ in range(n)]
d = [0] * 20002
for i in range(h):
    d[i] = min(d[i - a] + b for a, b in c)
print(d[h - 1])
