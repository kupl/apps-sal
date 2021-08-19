(N, T) = map(int, input().split())
t = list(map(int, input().split()))
X = T
for n in range(1, N):
    d = t[n] - t[n - 1]
    if d <= T:
        X += d
    else:
        X += T
print(X)
