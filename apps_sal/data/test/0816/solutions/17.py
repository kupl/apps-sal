read = lambda: list(map(int, input().split()))
from collections import Counter
n, x = read()
a = list(read())
c = Counter()
for i in a: c[i] += 1
cnt = 0
for i in a: cnt += c[i ^ x] - (x == 0)
cnt //= 2
print(cnt)

