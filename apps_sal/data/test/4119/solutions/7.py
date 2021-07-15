N, M, *X = list(map(int, open(0).read().split()))

if N >= M:
    print((0))
    return

X.sort()
diff = []
for i in range(M - 1):
    diff.append(X[i + 1] - X[i])
diff.sort()
print((sum(diff[: M - N])))


