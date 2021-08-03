import collections
S = list(input())
T = list(input())
counterS = collections.Counter(S)
counterT = collections.Counter(T)
Scou = list(counterS.values())
Tcou = list(counterT.values())
Scou.sort()
Tcou.sort()
if Scou == Tcou:
    print('Yes')
else:
    print('No')
