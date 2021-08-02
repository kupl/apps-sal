from collections import *
n = int(input())
c = Counter()

for i in list(map(int, input().split())):
    c[i] += 1
print("NO" if c.most_common(1)[0][1] > (n + 1) // 2 else "YES")
