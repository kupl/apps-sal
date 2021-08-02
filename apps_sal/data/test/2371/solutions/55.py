N, X, Y = map(int, input().split())
L = list(map(int, input().split()))
if N > 2:
    print(max(abs(L[-2] - L[-1]), abs(Y - L[-1])))
else:
    print(abs(L[-1] - Y))
