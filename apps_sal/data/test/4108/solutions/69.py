from collections import defaultdict

S = input()
T = input()

dictS = defaultdict(int)
dictT = defaultdict(int)
dictS[S[0]] = dictT[T[0]] = 1
n = 2

for i in range(1, len(S)):
    if dictS[S[i]] == dictT[T[i]]:
        if dictS[S[i]] == 0:
            dictS[S[i]] = dictT[T[i]] = n
            n += 1
    else:
        print('No')
        break
else:
    print('Yes')
