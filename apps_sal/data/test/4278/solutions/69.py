from collections import Counter
import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n = int(input())
l = [''.join(sorted(input())) for i in range(n)]
c = Counter(l).most_common()
ans = 0
for i in range(len(c)):
    if c[i][1] >= 2:
        ans += combinations_count(c[i][1], 2)
print(ans)
