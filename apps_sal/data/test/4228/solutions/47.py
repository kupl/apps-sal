(n, l) = map(int, input().split())
t = []
t2 = []
for i in range(n):
    taste = l + (i + 1) - 1
    t.append(taste)
    t2.append(taste ** 2)
oa = t[t2.index(min(t2))]
ans = sum(t) - oa
print(ans)
