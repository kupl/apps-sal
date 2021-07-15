n = int(input())
h = list(map(int, input().split()))

flag = False
ans = 0
while not flag:
  for i in range(n):
    if flag:
      if h[i] != 0: h[i] -= 1
      else: break
    elif not flag and h[i] != 0: 
      flag = True
      h[i] -= 1
      ans += 1
  if not flag: break
  flag = False
print(ans)  
