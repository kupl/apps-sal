N, X, Y = map(int, input().split())
ds = [0] * (N - 1)
 
for i in range(1, N):
    for j in range(i + 1, N + 1):
        d = min(j - i, abs(X - i) + 1 + abs(Y - j))
        ds[d - 1] += 1
 
for d in ds:
    print(d)
return
