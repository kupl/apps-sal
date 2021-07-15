from itertools import product

MOD = 10**9 + 7

L, R = list(map(int, input().split()))

binR = bin(R+1)[2:]
maxD = len(binR)
binL = bin(L-1)[2:].zfill(maxD)

dp = [[[[0]*(2) for k in range(2)] for j in range(2)] for i in range(maxD+1)]
dp[0][0][0][0] = 1
for d, (Ld, Rd) in enumerate(zip(binL, binR)):
    Ld, Rd = int(Ld), int(Rd)
    for isLleX, isYleR, isNum in product(list(range(2)), repeat=3):
        for x, y in [(0,0), (0,1), (1,1)]:
            if not isNum and (x, y) == (0, 1): continue
            if not isLleX and x < Ld: continue
            if not isYleR and y > Rd: continue
            isLleX2 = isLleX or x > Ld
            isYleR2 = isYleR or y < Rd
            isNum2 = isNum or y == 1
            dp[d+1][isLleX2][isYleR2][isNum2] += dp[d][isLleX][isYleR][isNum]
            dp[d+1][isLleX2][isYleR2][isNum2] %= MOD

print((dp[-1][1][1][1]))

