# 815A

inpt = input().split(" ")
n = int(inpt[0])
m = int(inpt[1])

arr = []

for i in range(n):
    inpt = input().split(" ")
    inpt = list(map(int, inpt))
    arr.append(inpt)

sol = []


def solver1(a, sol):
    allmin = min([min(suba) for suba in a])
    if allmin < 0:
        return False
    allmax = max([max(suba) for suba in a])
    if allmax == 0:
        return True
    else:
        for i in range(len(a)):
            p = min(a[i])
            if p > 0:
                for j in range(len(a[i])):
                    a[i][j] -= p
                for q in range(p):
                    sol.append(i + 1)
                return solver1(a, sol)
        for j in range(len(a[0])):
            b = []
            for i in range(len(a)):
                b.append(a[i][j])
            p = min(b)
            if p > 0:
                for k in range(len(b)):
                    a[k][j] -= p
                for q in range(p):
                    sol.append(len(a) + j + 1)
                return solver1(a, sol)


def solver2(a, sol):
    allmin = min([min(suba) for suba in a])
    if allmin < 0:
        return False
    allmax = max([max(suba) for suba in a])
    if allmax == 0:
        return True
    else:
        for j in range(len(a[0])):
            b = []
            for i in range(len(a)):
                b.append(a[i][j])
            p = min(b)
            if p > 0:
                for k in range(len(b)):
                    a[k][j] -= p
                for q in range(p):
                    sol.append(len(a) + j + 1)
                return solver2(a, sol)
        for i in range(len(a)):
            p = min(a[i])
            if p > 0:
                for j in range(len(a[i])):
                    a[i][j] -= p
                for q in range(p):
                    sol.append(i + 1)
                return solver2(a, sol)


if n < m:
    if solver1(arr, sol):
        print(len(sol))
        for i in sol:
            if i <= n:
                print("row", i)
            else:
                print("col", i - n)
    else:
        print("-1")
else:
    if solver2(arr, sol):
        print(len(sol))
        for i in sol:
            if i <= n:
                print("row", i)
            else:
                print("col", i - n)
    else:
        print("-1")
