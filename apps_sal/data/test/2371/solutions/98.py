(N, Z, W) = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    print(abs(W - A[0]))
else:
    ans = max(abs(A[-1] - W), abs(A[-1] - A[-2]))
    print(ans)
