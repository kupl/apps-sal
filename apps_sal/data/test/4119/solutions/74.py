N,M= map(int, input().split())
X= list(map(int, input().split()))

X.sort()

if N >= M:
    print(0)

elif N == 1:
    print(abs(max(X) - min(X)))

else:
    load = [X[i] - X[i - 1] for i in range(1, M)]
    load.sort()
    print(sum(load[:M - N]))
