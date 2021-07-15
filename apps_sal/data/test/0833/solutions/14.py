n, v = map(int, input().split())
s, t = 0, [0] * 3002
for i in range(n):
    a, b = map(int, input().split())
    t[a] += b
for d in range(1, 3002):
    ds = min(t[d - 1], v)
    s += ds
    ds = min(t[d], v - ds)
    t[d] -= ds
    s += ds
print(s)
