N = int(input())
S = sorted([int(a) for a in input().split()])
X = [1] + [0] * N


def popX(i0):
    for i in range(i0, N + 1):
        if X[i]:
            X[i] -= 1
            return i
    return N + 1


def addX():
    for l in L:
        for i in range(l + 1, N + 1):
            X[i] += 1


while S:
    a = S.pop()
    L = [popX(0)]
    while S and S[-1] == a:
        S.pop()
        L.append(popX(L[-1]))
    if L[-1] > N:
        print("No")
        break
    addX()
else:
    print("Yes")
