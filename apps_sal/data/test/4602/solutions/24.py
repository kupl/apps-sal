N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for i in x:
  ans += min(i, K - i) * 2
print(ans)
