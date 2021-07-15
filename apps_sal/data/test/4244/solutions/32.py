N = int(input())
X = list(map(int, input().split()))
MIN = 100**3

for i in range(min(X), max(X)+1):
  ans = 0
  for j in range(N):
    ans += ((X[j]-i)**2)
  if MIN > ans:
    MIN = ans

print(MIN)

