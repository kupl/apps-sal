N,Z,W = map(int,input().split())
A = list(map(int,input().split()))

ans = abs(W - A[-1])
if N > 1:
    a = abs(A[-2] - A[-1])
    ans = max(ans, a)
print(ans)
