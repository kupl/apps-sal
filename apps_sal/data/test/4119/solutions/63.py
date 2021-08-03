N, M = list(map(int, input().split()))
X = sorted(list(map(int, input().split())))
D = sorted([X[i + 1] - X[i] for i in range(M - 1)])
print((0 if M <= N else sum(D[:M - N])))
