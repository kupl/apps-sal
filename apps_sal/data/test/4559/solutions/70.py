N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
result = 1
for i in range(N):
  result *= A[i]
  if result > 10**18:
    result = -1
    break
print(result)
