n = int(input())
line = list(map(int, input().split()))
line.sort()
ans = (line[0] + line[1])/2
if n == 2:
  print(ans)
else:
  for i in range(2,n):
    ans = (ans + line[i]) / 2
  print(ans)
