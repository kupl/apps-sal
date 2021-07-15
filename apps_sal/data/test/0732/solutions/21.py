def dfs(num):
  if 0 < num <= n:
    s.add(num)
    num*=10
    dfs(num+x)
    dfs(num+y)

n = int(input())
s = set()
for x in range(10):
  for y in range(10):
    dfs(x)

print(len(s))

#Copied

