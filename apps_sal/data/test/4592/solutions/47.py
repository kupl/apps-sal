from operator import mul
from functools import reduce


def PrimeDecomp(N, ConcFlag):
    if ConcFlag:
        if N <= 1:
            return [1], 1
        else:
            I = 2
            PrimeDec = []
            DivCount = 1
            while I * I <= N:
                Cnt = 0
                while N % I == 0:
                    N //= I
                    PrimeDec.append(I)
                DivCount *= (Cnt + 1)
                I += 1
            if N >= 2:
                PrimeDec.append(N)
                DivCount *= 2
            return PrimeDec, DivCount
    else:
        if N <= 1:
            return [1], [1], 1
        else:
            I = 2
            PrimeDec = []
            PrimeCnt = []
            DivCount = 1
            while I * I <= N:
                Cnt = 0
                while N % I == 0:
                    N //= I
                    Cnt += 1
                if Cnt >= 1:
                    PrimeDec.append(I)
                    PrimeCnt.append(Cnt)
                    DivCount *= (Cnt + 1)
                I += 1
            if N >= 2:
                PrimeDec.append(N)
                PrimeCnt.append(1)
                DivCount *= 2
            return PrimeDec, PrimeCnt, DivCount


def DivisorFactorial(N, FactDec, FactCnt, MemoFlag):
    if MemoFlag:
        if N <= 1:
            FDivCnt = 1
            return FactDec, FactCnt, FDivCnt
        else:
            PrimeDec, PrimeCnt, _ = PrimeDecomp(N, False)
            for TP in range(0, len(PrimeDec)):
                if PrimeDec[TP] in set(FactDec):
                    FactCnt[FactDec.index(PrimeDec[TP])] += PrimeCnt[TP]
                else:
                    FactDec.append(PrimeDec[TP])
                    FactCnt.append(PrimeCnt[TP])
            FDivCnt = reduce(mul, [(T + 1) for T in FactCnt])
            return FactDec, FactCnt, FDivCnt
    else:
        if N <= 1:
            FDivCnt = 1
            return FactDec, FactCnt, FDivCnt
        else:
            for TN in range(2, N + 1):
                PrimeDec, PrimeCnt, _ = PrimeDecomp(TN, False)
                for TP in range(0, len(PrimeDec)):
                    if PrimeDec[TP] in set(FactDec):
                        FactCnt[FactDec.index(PrimeDec[TP])] += PrimeCnt[TP]
                    else:
                        FactDec.append(PrimeDec[TP])
                        FactCnt.append(PrimeCnt[TP])
            FDivCnt = reduce(mul, [(T + 1) for T in FactCnt])
            return FactDec, FactCnt, FDivCnt


N = int(input())
FactDec, FactCnt, FDivCnt = DivisorFactorial(N, [], [], False)
print(FDivCnt % (10**9 + 7))
