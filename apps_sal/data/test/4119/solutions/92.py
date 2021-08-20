(N, M) = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()
cnt = 0
arr = [0] * (M - 1)
if N >= M:
    ans = 0
else:
    for i in range(1, M):
        arr[i - 1] = abs(X[i - 1] - X[i])
    arr.sort()
    ans = sum(arr[0:M - N])
print(ans)
