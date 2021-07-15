n = int(input())
a = list(map(int, input().split()))
from collections import Counter
a = Counter(a)
lis = []

for i,j in a.items():
    lis += [i]*(j//2)

#print(lis)

lis.sort(reverse=True)
if len(lis) <= 1:
    ans = 0
else:
    ans = lis[0]*lis[1]

print(ans)
