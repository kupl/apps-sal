from collections import Counter
n,*a = map(int,open(0).read().split())
s = set(a)
c = Counter(a)
m = max(s)
l = [True]*(m+1)
ans = 0
for i in range(1,m+1):
  if i in s and l[i]:
    if c[i] == 1:
      ans += 1
    for j in range(1,m//i+1):
      l[i*j] = False
print(ans)
