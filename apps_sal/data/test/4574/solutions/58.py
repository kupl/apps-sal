from collections import defaultdict

d = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))

ans = []
for i in a:
  d[i] += 1
  if d[i] == 2:
    d[i] = 0
    ans.append(i)
ans.sort(reverse=True)
if len(ans) >= 2:
  print((ans[0]*ans[1]))
else:
  print((0))

