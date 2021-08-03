N, K = [int(x) for x in input().split()]
minA = 2
maxA = 2 * N
minC = 2
maxC = 2 * N
minA = max(minA, K + minC)
maxA = min(maxA, K + maxC)
ans = 0
for i in range(minA, maxA + 1):
    C = i - K
    mina = i - N
    maxa = i - 1
    if mina < 1:
        mina = 1
    if maxa > N:
        maxa = N
    cntA = maxa - mina + 1
    minc = C - N
    maxc = C - 1
    if minc < 1:
        minc = 1
    if maxc > N:
        maxc = N
    cntC = maxc - minc + 1
    ans += cntA * cntC
print(ans)
