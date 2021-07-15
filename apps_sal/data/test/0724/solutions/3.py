n, d = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
l=0
r = 0
ans = 0
while r < n:
    if a[r]-a[l] <= d:
        ans= max(ans, r-l+1)
        r += 1
    else:
        l+=1
print(n-ans)
