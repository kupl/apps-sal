
from collections import Counter
n = int(input())
a = list(map(int, input().split()))

# a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
# n=len(a)

a.sort()

a = Counter(a)
csum = 0
for i, icnt in a.most_common():
    csum += icnt - 1
if csum % 2 == 1:
    csum += 1
print((n - csum))
