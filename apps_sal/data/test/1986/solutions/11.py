n,k = list(map(int, input().split()))
rest = []
for cont in range(0,n):
    l = list(map(int, input().split()))
    rest.append(l)

maxjoy = -9999999999999999
for r in rest:
    if r[1] > k:
        joy = r[0]-r[1] +k
    else:
        joy = r[0]
    if joy > maxjoy:
        maxjoy = joy
print(maxjoy)

