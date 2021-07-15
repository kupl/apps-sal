K, N = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N-1):
  B.append(A[i+1] - A[i])
B.append(K - A[N-1] + A[0])
ans = K - max(B)
print(ans)
