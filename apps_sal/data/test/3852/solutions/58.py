N = int(input())
A = list(map(int,input().split()))

if all(a==0 for a in A):
    print(0)
    return

INF = float('inf')
mn = INF
mx = -INF
mni = mxi = -1
for i,a in enumerate(A):
    if a > mx:
        mx = a
        mxi = i
    if a < mn:
        mn = a
        mni = i

ans = []
if mn >= 0:
    p = True
elif mx <= 0:
    p = False
else:
    if mx > -mn:
        for i,a in enumerate(A):
            if a < 0:
                ans.append((mxi+1, i+1))
        p = True
    else:
        for i,a in enumerate(A):
            if a > 0:
                ans.append((mni+1, i+1))
        p = False

if p:
    for i in range(1,N):
        ans.append((i,i+1))
else:
    for i in range(N,1,-1):
        ans.append((i,i-1))

print(len(ans))
for a,b in ans:
    print(a,b)
