N, X = (int(T) for T in input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(0, N - 1):
    if A[i] + A[i + 1] > X:
        s = A[i] + A[i + 1] - X
        ans = s + ans
        A[i] = A[i] - max(0, A[i] - A[i + 1])
        A[i + 1] = max(0, A[i + 1] - s)
print(ans)
