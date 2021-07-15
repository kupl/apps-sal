n = int(input())
light = [0] * (n+1)

for i in range(1,n+1):
  light[i] = int(input())
s = 1
ans = 0
while light[s] != 2 and ans <= n:
  s = light[s]
  ans += 1

if light[s] == 2:
  print(ans + 1)
else:
  print(-1)
