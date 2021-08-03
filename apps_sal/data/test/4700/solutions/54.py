n, m = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
a, b = [], []
for i in range(m):
    a1, b1 = [int(x) for x in input().split()]
    a.append(a1 - 1)
    b.append(b1 - 1)
ans = [1] * n
for i in range(m):
    if h[a[i]] < h[b[i]]:
        ans[a[i]] = 0
    elif h[a[i]] > h[b[i]]:
        ans[b[i]] = 0
    else:
        ans[a[i]] = 0
        ans[b[i]] = 0
c = 0
for i in range(n):
    if ans[i] == 1:
        c += 1
# print(ans)
print(c)
