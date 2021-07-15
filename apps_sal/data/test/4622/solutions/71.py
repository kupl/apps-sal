import collections
n = int(input())
aa = list(map(int, input().split()))
c =collections.Counter(aa)
if len(c) == n:
  print('YES')
else:
  print('NO')
