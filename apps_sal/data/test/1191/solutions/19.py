n, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = [x for x in range(n)]
zz = sorted(zip(x, y, z))
pre = []
c = 1
f = [0] * n
vv = 0
# print(zz)
# print(pre)
ss = 0
for i in range(n):
    if(i < k):
        pre.append(zz[i][1])
        gh = int(zz[i][2])
        f[gh] = ss + zz[i][1]
        ss += zz[i][1]
    else:
        pre.sort()
        gh = int(zz[i][2])
        f[gh] = ss + zz[i][1]
        ff = False
        for j in range(0, len(pre)):
            if(zz[i][1] > pre[j]):
                ff = True
                ss = ss - pre[j] + zz[i][1]
                pre[j] = zz[i][1]
                break
print(*f)
