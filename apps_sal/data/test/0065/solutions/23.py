def lInt(d=None):
    return list(map(int, input().split(d)))


(n, *_) = lInt()
a = list(lInt())
mini = min(a)
p = []
ans = 10000000
for (i, v) in enumerate(a):
    if v == mini:
        p.append(i)
for (i, j) in enumerate(p):
    if i > 0 and p[i] - p[i - 1] < ans:
        ans = p[i] - p[i - 1]
print(ans)
