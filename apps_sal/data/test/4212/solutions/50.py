from itertools import combinations_with_replacement
n,m,q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

nums = combinations_with_replacement(range(1,m+1), n)
ans = 0
for a in nums:
  t = 0
  for i in abcd:
    if a[i[1]-1] - a[i[0]-1] == i[2]: t += i[3]
  if ans < t: ans = t
print(ans)
