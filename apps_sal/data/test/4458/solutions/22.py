n = int(input())
P = list(map(int,input().split()))
mi = P[0]
ans = 0
for i in range(n):
  if P[i] <= mi:
    ans += 1
    mi = P[i]
print(ans)
