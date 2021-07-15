import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N = int(input())
Comlist = []
Ans = dict()
Answer = 0
for i in range(1,10):
    for j in range(1,10):
        M = i*10 + j
        Comlist.append(str(M))
        Ans[str(M)] = 0
for k in range(1,N+1):
    strk = str(k)
    if k < 10:
        Tar = strk + strk
        Ans[Tar] += 1
    else:
        Tar = strk[0] + strk[-1]
        if Tar in Ans:
            Ans[Tar] += 1
Answer = 0
for q in range(len(Comlist)):
    p = Comlist[q]
    pin = p[1] + p[0]
    Answer += Ans[p] * Ans[pin]
print(Answer)
