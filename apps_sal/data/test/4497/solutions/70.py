def solve(n):
  res = 0
  while(n != 1):
    if n%2 == 0:
      res += 1
      n /= 2
    else:
      break
  return res

n = int(input())

ans = 1
ans_max = 0
for i in range(1, n+1):
  cnt = solve(i)
  if cnt > ans_max:
    ans_max = cnt
    ans = i
print(ans)
