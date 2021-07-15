import math
n, m = map(int,input().split())
a = list(map(int,input().split()))
count = 0

for i in range(n):
    if a[i] >= math.ceil(sum(a) / (4 * m)):
        count += 1
if count >= m:
    print('Yes')
else:
    print('No')
