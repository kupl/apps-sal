import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = 0
for (value, count) in counter.items():
    if value - 1 in counter:
        count += counter[value - 1]
    if value + 1 in counter:
        count += counter[value + 1]
    ans = max(ans, count)
print(ans)
