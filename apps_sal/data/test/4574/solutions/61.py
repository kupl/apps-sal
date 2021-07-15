n = int(input())
a1 = list(map(int, input().split()))
from collections import Counter
a = Counter(a1).most_common()
l = []
for i in range(len(a)):
    if 2 <= a[i][1]:
        for h in range(a[i][1]//2):
            l.append(a[i][0])
l.sort()
if 2 <= len(l):
    print(l[-1]*l[-2])
else:
    print(0)
