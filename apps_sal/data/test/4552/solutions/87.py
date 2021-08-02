def ForBaseConvert(Roop, MaxD, Base):
    if all(type(TT) is int for TT in [Roop, MaxD, Base]):
        if Base >= 2 and MaxD >= 1:
            ConvertN = []
            while Roop > 0:
                ConvertN.append(Roop % Base)
                Roop = Roop // Base

            BaseConv = [0] * (MaxD - len(ConvertN)) + ConvertN[::-1]
            BaseSInd = [[] for TB in range(0, Base)]
            for TB in range(0, Base):
                BaseSInd[TB] = [SInd for SInd, SNum in enumerate(BaseConv) if SNum == TB]
            return BaseConv, BaseSInd
        else:
            return []
    else:
        return []


N = int(input())
F = [[] for TF in range(0, N)]
for TF in range(0, N):
    F[TF] = [int(T) for T in input().split()]
P = [[] for TP in range(0, N)]
for TP in range(0, N):
    P[TP] = [int(T) for T in input().split()]

MAXB = -10**9
for TB in range(1, 2**10):
    BaseConv, BaseSInd = ForBaseConvert(TB, 10, 2)
    Benefit = 0
    for TN in range(0, N):
        Count = sum(1 if F[TN][TT] == 1 else 0 for TT in BaseSInd[1])
        Benefit += P[TN][Count]
    if MAXB < Benefit:
        MAXB = Benefit
print(MAXB)
