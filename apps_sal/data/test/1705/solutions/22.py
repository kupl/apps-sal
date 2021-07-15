n = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(n-1, -1, -1):
  if A[i] != A[n-1]:
    ans = i+1
    break
print(ans)

