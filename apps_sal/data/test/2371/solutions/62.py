(N, _, W) = map(int, input().split())
A = [int(i) for i in input().split()]
if N == 1:
    ans = abs(A[0] - W)
else:
    ans = abs(A[-1] - A[-2])
    ans = max(ans, abs(A[-1] - W))
print(ans)
