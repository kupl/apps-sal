N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
Y = [X[i] - X[i-1] for i in range(1, M)]
Y.sort(reverse=True)
Y = Y[N-1:]
print(sum(Y))
