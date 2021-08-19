N = int(input())
X = list(map(int, input().split()))
Xs = sorted(X)
c = int(N / 2)
(a, b) = (Xs[c - 1], Xs[c])
for i in range(N):
    if X[i] <= a:
        print(b)
    else:
        print(a)
