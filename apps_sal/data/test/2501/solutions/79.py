n = int(input())
a = list(map(int,input().split()))

x = [ aa + i  for i,aa in enumerate(a,start = 1)]
y = [ i - aa  for i,aa in enumerate(a,start = 1)]

from collections import Counter
c = Counter(y)
ans = 0
for xx in x:
    ans += c[xx]
print(ans)




