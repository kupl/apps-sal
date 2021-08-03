import numpy as np
S = np.array(list(input()))
T = np.array(list(input()))
N = len(S)
SSrt = np.sort(S)
TSrt = np.sort(T)
SArg = np.argsort(S)
TArg = np.argsort(T)
SAgT = S[TArg]
TAgS = T[SArg]

SBef = ''
TBef = ''
SFlag = True
for ST in range(0, N):
    SNow = SSrt[ST]
    TNow = TAgS[ST]
    if SBef == SNow:
        if TBef != TNow:
            SFlag = False
            break
    SBef = SNow
    TBef = TNow

SBef = ''
TBef = ''
TFlag = True
for TT in range(0, N):
    SNow = SAgT[TT]
    TNow = TSrt[TT]
    if TBef == TNow:
        if SBef != SNow:
            TFlag = False
            break
    SBef = SNow
    TBef = TNow

if SFlag and TFlag:
    print('Yes')
else:
    print('No')
