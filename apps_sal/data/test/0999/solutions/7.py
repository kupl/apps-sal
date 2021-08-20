n = int(input())
(mnc, mxc, mnp, mxp) = (10000000000.0, 0, 10000000000.0, 0)
for i in range(n):
    (a, b) = list(map(int, input().split()))
    mxc = max(mxc, a)
    mnc = min(mnc, b)
n2 = int(input())
for i in range(n2):
    (a, b) = list(map(int, input().split()))
    mxp = max(mxp, a)
    mnp = min(mnp, b)
val = max(mxp - mnc, mxc - mnp)
if val < 0:
    print(0)
else:
    print(val)
