import collections
n = int(input())
S = list(input())
counterA = collections.Counter(S)
for i in range(1,n):
    counterB = collections.Counter()
    S = list(input())
    counterS = collections.Counter(S)
    for j in counterA.keys():
        if j in counterS:
            counterB[j] = min(counterA[j],counterS[j])
        else:
            counterB[j] = 0
    counterA = counterB
ls = []
for i in counterA.keys():
    for j in range(counterA[i]):
        ls.append(i)
ls.sort()
ans = ''.join(ls)
print(ans)
