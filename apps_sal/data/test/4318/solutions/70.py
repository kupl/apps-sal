n = int(input())
h = list(map(int, input().split()))
ans = 0
highest = h[0]
for i in range(n):
  if highest <= h[i]:
    ans += 1
    highest = h[i]
print(ans)
