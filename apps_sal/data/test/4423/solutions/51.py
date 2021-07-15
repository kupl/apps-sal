N = int(input())
city = []
score = dict()
arr = []
for i in range(N):
  c, s = input().split()
  arr.append([c, int(s)])
  city.append(c)
  if c in score:
    score[c].append(int(s))
  else:
    score[c] = [int(s)]
city.sort()
ans = []
for i, var in enumerate(city):
  t = score[var].index(max(score[var]))
  u = score[var].pop(t)
  ans.append(arr.index([var,u]) + 1)
for i in ans:
  print(i)
