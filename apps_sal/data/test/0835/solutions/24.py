inf = 100000000000000

ch = input()
B = sum(x == 'B' for x in ch)
S = sum(x == 'S' for x in ch)
C = sum(x == 'C' for x in ch)

a = [int(x) for x in input().split()]
nb = a[0]
ns = a[1]
nc = a[2]

a = [int(x) for x in input().split()]
pb = a[0]
ps = a[1]
pc = a[2]


if B == 0:
    pb = 0
    B = 1
    nb = inf

if S == 0:
    ps = 0
    S = 1
    ns = inf

if C == 0:
    pc = 0
    C = 1
    nc = inf

R = int(input())

l = min(nb//B , ns//S , nc//C)
r = inf
ans = l

def ck(z):
    v = max(0,(B*z-nb)*pb) + max(0,(S*z-ns)*ps) + max(0,(C*z-nc)*pc)
    if v <= R:
        return 1
    return 0

while l <= r:
    mid = (l+r)>>1
    if ck(mid):
        ans = mid
        l = mid+1
    else:
        r = mid-1
print(ans)
###

