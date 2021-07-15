import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = 0
for e in c:
  if e < c[e]:
    ans += c[e] - e
  elif e > c[e]:
    ans += c[e]
print(ans)
