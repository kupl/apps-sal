"""
in1 = '7 4 4'
in2 = ['1 2', '2 3', '2 5', '6 7', '3 5', '4 5', '3 4', '6 7']
N, K, L = map(int, in1.split())
pqrs = []
for idx1 in range(K + L):
    temp0, temp1 = map(int, in2[idx1].split())
    pqrs.append([temp0, temp1])
"""

def makeTree(a):
    aT = list(range(N + 1))
    for p, q in a:
        rootp     = getRoot(aT, p)
        rootq     = getRoot(aT, q)
        thisRoot  = max(rootp, rootq, q)
        aT[p]     = thisRoot
        aT[q]     = thisRoot
        aT[rootp] = thisRoot
        aT[rootq] = thisRoot
    return aT

def getRoot(a,i):
    if a[i] == i:
        return i
    else:
        a[i] = getRoot(a, a[i])
        return a[i]

N, K, L = list(map(int, input().split()))
pqrs = []
for idx1 in range(K + L):
    temp0, temp1 = list(map(int, input().split()))
    pqrs.append([temp0, temp1])

MTree = makeTree(pqrs[0:K])
TTree = makeTree(pqrs[K:])

aRet = []
dRet = {}
for idx1 in range(1, N + 1):
    Comb = (getRoot(MTree, idx1), getRoot(TTree, idx1))
    aRet.append(Comb)
    if Comb in dRet:
        dRet[Comb] += 1
    else:
        dRet[Comb] = 1

print((" ".join([str(dRet[_]) for _ in aRet])))

