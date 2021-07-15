N = int(input())
A = list(map(int, input().split()))
result = 'APPROVED'
for i in range(N):
  if A[i]%2 == 0 and A[i]%3 != 0 and A[i]%5 != 0:
    result = 'DENIED'
    break
print(result)
