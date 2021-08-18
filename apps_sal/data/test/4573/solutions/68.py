import copy

N = int(input())
X = list(map(int, input().split()))


X = [[i, x] for i, x in enumerate(X)]
X = sorted(X, reverse=False, key=lambda x: x[1])
X_ranked = copy.copy(X)
X = [[l[0], i, l[1]] for i, l in enumerate(X)]
X = sorted(X, reverse=False, key=lambda x: x[0])

med = len(X) // 2

for l in X:
    if l[1] < med:
        print((X_ranked[med][1]))
    else:
        print((X_ranked[med - 1][1]))
