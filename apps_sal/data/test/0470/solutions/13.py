t = list(map(int, input().split()))
p = sum(t)
for i in range(5):
    if t.count(t[i]) >= 2:
        p = min(p, sum(t) - t[i] * 2)
for i in range(5):
    if t.count(t[i]) >= 3:
        p = min(p, sum(t) - t[i] * 3)
print(p)

