import numpy as np

iNum = int(input())
naXY = np.zeros((iNum, 2))
for iI in range(iNum):
    x, y = list(map(int, input().split()))
    naXY[iI] = [x, y]
naXY0 = np.average(naXY, axis=0) + np.random.rand(2) * 1e-3
fA = 1.0e-1
while fA > 1.0e-10:
    naP = naXY - naXY0
    naR = np.einsum("ij, ij -> i", naP, naP)
    iImax = np.argmax(naR)
    naE = naP[iImax]
    naXY0 += naE * fA
    fA *= 0.9998
print((naR[iImax]**0.5))
