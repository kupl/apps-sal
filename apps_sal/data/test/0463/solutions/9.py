(n, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 100
o = set()
c = set()
for i in range(n):
    if a[i] in o:
        ans = min(ans, 0)
    elif a[i] in c:
        ans = min(ans, 1)
    elif a[i] & x in o:
        ans = min(ans, 1)
    elif a[i] & x in c:
        ans = min(ans, 2)
    o.add(a[i])
    c.add(a[i] & x)
print(-1 if ans == 100 else ans)
