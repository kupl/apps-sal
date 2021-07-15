from operator import mul

def getMatrixProduct(Ass, Bss, MOD):
    BssTr = [list(Bs) for Bs in zip(*Bss)]  # 転置
    ansss = [[sum(map(mul, As, Bs)) % MOD for Bs in BssTr] for As in Ass]
    return ansss

def getMatrixPower(Ass, n, MOD):
    sizeA = len(Ass)
    ansss = [[0]*(sizeA) for _ in range(sizeA)]
    for i in range(sizeA):
        ansss[i][i] = 1
    while n:
        if n & 1:
            ansss = getMatrixProduct(ansss, Ass, MOD)
        Ass = getMatrixProduct(Ass, Ass, MOD)
        n //= 2
    return ansss

L, A, B, M = list(map(int, input().split()))

As = [[A%M], [A%M], [1]]
iPrev = 0
d = 1
while True:
    i = (10**d-1-A) // B
    if i > L-1:
        i = L-1
    num = i-iPrev
    if num > 0:
        Css = [[10**d,1,B%M], [0,1,B%M], [0,0,1]]
        PowCss = getMatrixPower(Css, num, M)
        As = getMatrixProduct(PowCss, As, M)
    if i == L-1:
        break
    iPrev = max(0, i)
    d += 1

print((As[0][0]))

