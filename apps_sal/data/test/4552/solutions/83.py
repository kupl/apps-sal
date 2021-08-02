import numpy as np
N = int(input())

F = np.empty((N, 10))
P = np.empty((N, 11))
for i in range(N):
    Flist = np.array(list(map(int, input().split())), dtype=int)
    F[i] = Flist
for i in range(N):
    Plist = np.array(list(map(int, input().split())), dtype=int)
    P[i] = Plist
BenefitMax = 0

for i in range(1, 1024):
    A = np.zeros(10)
    iForBin = i
    for j in range(10):
        if iForBin % 2 == 1:
            A[j] = 1
        iForBin = iForBin // 2
    ADotF = np.tensordot(A, F, ((0), (1)))
    Benefit = 0
    for j in range(N):
        Benefit += P[j, int(ADotF[j])]
    if i == 1:
        BenefitMax = Benefit
    else:
        if BenefitMax < Benefit:
            BenefitMax = Benefit

print(int(BenefitMax))
