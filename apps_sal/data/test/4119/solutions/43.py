(N, M) = map(int, input().split())
X = sorted(list(map(int, input().split())))
h = []
ans = 0
if N < M:
    for i in range(M - 1):
        h.append(X[i + 1] - X[i])
    h = sorted(h)
    ans = max(ans, sum(h[:M - N]))
print(ans)
