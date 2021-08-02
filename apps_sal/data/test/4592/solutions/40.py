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


def DivisorFactorial(N, FactDec, FactCnt, MemoFlag, Mod, ModFlag):
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
            FDivCnt = 1
            for TF in FactCnt:
                FDivCnt = [FDivCnt * (TF + 1), (FDivCnt * (TF + 1)) % Mod][ModFlag]
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
            FDivCnt = 1
            for TF in FactCnt:
                FDivCnt = [FDivCnt * (TF + 1), (FDivCnt * (TF + 1)) % Mod][ModFlag]
            return FactDec, FactCnt, FDivCnt


FactDec, FactCnt, FDivCnt = DivisorFactorial(int(input()), [], [], False, 10**9 + 7, True)
print(FDivCnt)
