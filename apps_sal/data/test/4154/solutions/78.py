(n, m) = map(int, input().split())
s = 0
t = 10 ** 10
for i in range(m):
    (l, r) = map(int, input().split())
    s = max(s, l)
    t = min(t, r)
if s > t:
    print(0)
else:
    print(t - s + 1)
