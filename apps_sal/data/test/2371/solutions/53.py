N, Z, W = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

ans = max(abs(A[N-2]-A[N-1]), abs(A[N-1]-W))
print(ans)
