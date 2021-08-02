import math


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


D, G = (int(T) for T in input().split())
PCList = [[] for TD in range(0, D)]
MINSolve = 1000
for TD in range(0, D):
    PCList[TD] = [int(T) for T in input().split()]

for Roop in range(0, 2**D):
    Failed = False
    BaseConv, BaseSInd = ForBaseConvert(Roop, D, 2)
    Solve = 0
    Point = 0
    for TD in range(0, D):
        if BaseConv[TD] == 1:
            Solve += PCList[TD][0]
            Point += (100 * (TD + 1) * PCList[TD][0]) + PCList[TD][1]

    if len(BaseSInd[0]) > 0:
        Add = BaseSInd[0][-1]
        Ned = math.ceil(max(G - Point, 0) / (100 * (Add + 1)))
        if Ned <= (PCList[Add][0] - 1):
            Solve += Ned
            Point += 100 * (Add + 1) * Ned

    if Point >= G and Solve < MINSolve:
        MINSolve = Solve
print(MINSolve)
