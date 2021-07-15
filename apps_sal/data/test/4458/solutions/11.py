N = int(input())
P = list(map(int, input().split()))

ans = 0
m = float("inf")
for i in range(N):
  if P[i] <= m:
    ans += 1
    m = P[i]
print(ans)
