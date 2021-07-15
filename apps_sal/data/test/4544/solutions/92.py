n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n):
    b += [a[i],a[i]+1,a[i]-1]
import collections
c = collections.Counter(b)
print(c.most_common()[0][1])
