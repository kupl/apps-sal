x,y,l,r = list(map(int, input().split()))
xx = 1
a = [0, 1e20]
for i in range(60):
    yy = 1
    while xx + yy <= r:
        a.append(xx+yy)
        yy *= y
    xx *= x
a.sort()
ans = 0
for i in range(len(a)-1):
    ll = max(a[i]+1, l)
    rr = min(a[i+1]-1, r)
    ans = max(ans, rr - ll+1)
    #~ print(i, ans, a[i], a[i+1])
print(ans)

