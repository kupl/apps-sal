n = int(input())
s = list(map(int, input().split()))
ans = 0
for i in range(n):
  while s[i] %2 == 0:
    s[i] /= 2
    ans += 1

print(ans)
