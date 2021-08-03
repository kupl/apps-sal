def I(): return list(map(int, input().split()))


k, n = I()
a, b = list(I()), list(I())
s = 0
for i in range(k):
    s += a[i]
    a[i] = s
# print(a)
ans = [set() for x in range(n)]
for i, y in enumerate(b):
    ans[i] = [y - x for x in a]
# print(ans)
ans2 = set(ans[0])
# print(ans2)
for x in ans:
    ans2.intersection_update(x)
# print(ans2)
print(len(ans2))
