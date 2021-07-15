n,m = map(int, input().split())
s = [list(map(lambda x: int(x)-1, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
  for x,y in zip(s,p):
    flag = False
    for a in x:
      if i>>a&1: flag = not flag
    if int(flag) != y: break
  else: ans += 1
print(ans)
