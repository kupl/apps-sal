n = int(input())
line = list(map(int, input().split()))
ans = 30
for i in range(n):
  count = 0
  x = line[i]
  while True:
    if x % 2 == 0:
      x = x//2
      count += 1
    else:
      break
  if count < ans:
    ans = count
print(ans)
      

