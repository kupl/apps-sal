import sys

def solve():
    input = sys.stdin.readline
    N, A, R, M = map(int, input().split())
    H = [int(h) for h in input().split()]
    H.sort()
    tB = [0] * (N + 1)
    for i, h in enumerate(H): tB[i+1] = tB[i] + h
    minCost = 10 ** 20
    for i in range(N):
        toAdd = H[i] * i - tB[i]
        toSub = tB[N] - tB[i+1] - H[i] * (N - i - 1)
        if M >= A + R: minCost = min(minCost, A * toAdd + R * toSub)
        else:
            mN = min(toAdd, toSub)
            minCost = min(minCost, A * (toAdd - mN) + R * (toSub - mN) + M * mN)
    if M < A + R:
        sumH = sum(H)
        lcost = 0
        hcost = 0
        fH = sumH // N
        for i, h in enumerate(H):
            if h < fH: lcost += (fH - h) * M
            if h > fH + 1: hcost += (h - fH - 1) * M
        lcost += (sumH % N) * R
        hcost += (N - (sumH % N)) * A
        minCost = min(minCost, lcost)
        minCost = min(minCost, hcost)
    
    print(minCost)

    return 0

def __starting_point():
    solve()
__starting_point()
