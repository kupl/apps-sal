t = int(input())
for _ in range(t):
  x = int(input())
  ans = 0
  size = 1
  temp = (size*(size+1))//2
  while x >= temp:
    ans += 1
    x -= temp
    size = 2*size + 1
    temp = (size*(size+1))//2
  print(ans)

