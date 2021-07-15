N = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(N):
  for j in range(i+1, N):
    if i != j:
      ans += d[i] * d[j]
print(ans)
