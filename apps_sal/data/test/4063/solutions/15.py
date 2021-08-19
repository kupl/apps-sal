(N, *D) = map(int, open(0).read().split())
D.sort()
n = N // 2
print(D[n] - D[n - 1])
