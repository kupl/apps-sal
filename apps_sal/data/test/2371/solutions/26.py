(n, z, w) = map(int, input().split())
A = list(map(int, input().split()))
ans = max(abs(A[-2] - A[-1]) if len(A) > 1 else 0, abs(A[-1] - w))
print(ans)
