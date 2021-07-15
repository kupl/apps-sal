import collections
S = list(input())
D = collections.Counter(S)
ans = 'Yes'

for v in D.values():
  if v % 2 != 0:
    ans = 'No'
    break

print(ans)
