n = int(input())
vl, vr = 0, 0
for i in range(n):
    l, r = (int(x) for x in input().split())
    vl += l
    vr += r
print(min(vl, n - vl) + min(vr, n - vr))
