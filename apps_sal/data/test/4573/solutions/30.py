N = int(input())
X = [int(i) for i in input().split()]
Xs = list(sorted(X))
for x in X:
    if x > Xs[N // 2 - 1]:
        print(Xs[N // 2 - 1])
    else:
        print(Xs[N // 2])
