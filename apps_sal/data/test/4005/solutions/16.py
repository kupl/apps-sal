a=[*map(int,input().split())]
b=[*map(int,input().split())]
c=[*map(int,input().split())]

ab=[0]*4
ab[0] = max(a[0],b[0])
ab[2] = min(a[2],b[2])
ab[1] = max(a[1],b[1])
ab[3] = min(a[3],b[3])

# print(ab)
if ab==a:
    print("NO")
    return

ac=[0]*4
ac[0] = max(a[0],c[0])
ac[2] = min(a[2],c[2])
ac[1] = max(a[1],c[1])
ac[3] = min(a[3],c[3])

# print(ac)
if ac==a:
    print("NO")
    return

if ab[0]>=ab[2] or ab[1]>=ab[3] or ac[0]>=ac[2] or ac[1]>=ac[3]:
    print("YES")
    return

abac=[0]*4
abac[0] = max(ab[0],ac[0])
abac[2] = min(ab[2],ac[2])
abac[1] = max(ab[1],ac[1])
abac[3] = min(ab[3],ac[3])

oo=(ab[2]-ab[0])*(ab[3]-ab[1])+(ac[2]-ac[0])*(ac[3]-ac[1])
if abac[0]>=abac[2] or abac[1]>=abac[3]:
    oo-=0
else:
    oo-=(abac[2]-abac[0])*(abac[3]-abac[1])

if oo>=(a[2]-a[0])*(a[3]-a[1]):
    print("NO")
else:
    print("YES")
