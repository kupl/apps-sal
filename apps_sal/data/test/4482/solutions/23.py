N = int(input())
A = list(map(int,input().split()))

min_a = min(A)
max_a = max(A)

ans = float("inf")
for i in range(min_a, max_a+1):
  tmp = 0
  for j in A:
    tmp += (i - j) ** 2
  ans = min(ans, tmp)
  
print(ans)
