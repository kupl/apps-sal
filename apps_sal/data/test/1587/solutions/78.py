import collections
n = int(input())
wr = list(input())
cc = collections.Counter(wr)
r = cc['R']
ans = wr[:r].count('W')
print(ans)
