import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = 0
for k in c.keys():
  if k > c[k]:
    ans += c[k]
  elif k < c[k]:
    ans += c[k] - k
print(ans)
