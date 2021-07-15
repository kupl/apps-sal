N = int(input())
K = int(input())
x = list(map(int,input().split()))
ans = 0

for i in range(N):
  ans += min(abs(x[i] - 0), abs(K - x[i]))
print(ans * 2)
