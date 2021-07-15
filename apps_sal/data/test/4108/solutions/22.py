import collections
S = list(input())
T = list(input())
 
cntS = collections.Counter(S)
cntT = collections.Counter(T)
 
if len(cntS) != len(cntT):
    print('No')
    return
else:
    valS = list(cntS.values())
    valT = list(cntT.values())

    if valS != valT:
            print('No')
            return
print('Yes')
