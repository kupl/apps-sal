n, m = list(map(int,input().split()))
a = []
s = 0
for i in range(n):
    k, b = list(map(int,input().split()))
    s += k
    a.append(k - b)
a.sort(reverse=True)
ans = 0
for i in range(n):
    if s <= m:
        print(ans)
        return
    s -= a[i]
    ans += 1
if s <= m:
    print(ans)
else:
    print(-1)

