l1,r1,l2,r2,k = (int(i) for i in input().split())
l = max(l1,l2)
r = min(r1,r2)
if r < l:
    print(0)
else:
    ans = r-l
    if k >= l and k <= r:
        print(ans)
    else:
        print(ans+1)
