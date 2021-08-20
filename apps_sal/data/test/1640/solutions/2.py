from collections import Counter
from itertools import accumulate as acc


def read():
    return list(map(int, input().split()))


n = int(input())
x = read()
s = 0
ans = 0
c = Counter()
for (num, i) in enumerate(x):
    ans += (num - c[i - 1] - c[i + 1]) * i - (s - c[i - 1] * (i - 1) - c[i + 1] * (i + 1))
    c[i] += 1
    s += i
print(ans)
