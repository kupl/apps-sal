X = dict()
Y = dict()
A = set()

for i in range(8):
    x, y = list(map(int, input().split()))

    if (x, y) in A:
        print('ugly')
        return
    else:
        A.add((x, y))

    if x in X:
        X[x] += 1
    else:
        X[x] = 1

    if y in Y:
        Y[y] += 1
    else:
        Y[y] = 1

X = [(i, X[i]) for i in X]
Y = [(i, Y[i]) for i in Y]
X.sort()
Y.sort()

if len(X) == 3 and len(Y) == 3 and X[0][1] == 3 and X[1][1] == 2 and X[2][1] == 3 and Y[0][1] == 3 and Y[1][1] == 2 and Y[2][1] == 3:
    print('respectable')
else:
    print('ugly')
