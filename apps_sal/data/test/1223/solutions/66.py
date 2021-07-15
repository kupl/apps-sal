N = int(input())
Ps = list(map(int, input().split()))

iPs = [0] * (N+1)
for iP, A in enumerate(Ps):
    iPs[A] = iP

ans = 0
iLs = list(range(N+1))
iRs = list(range(N+1))
for P in range(1, N+1):
    i = iPs[P]
    iL, iR = iLs[i], iRs[i]
    if iL <= 1:
        iL2 = 0
    else:
        iL2 = iLs[iL-1]
    if iR >= N-2:
        iR2 = N-1
    else:
        iR2 = iRs[iR+1]
    num = 0
    if iL != 0:
        num += (iL-iL2)*(iR-i+1)
    if iR != N-1:
        num += (i-iL+1)*(iR2-iR)
    ans += P * num
    iLs[iR+1] = iL
    iRs[iL-1] = iR

print(ans)

