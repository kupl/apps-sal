import sys
from collections import Counter

arr = list(map(int, input().split()))

d = Counter(arr)

temp = [min(v, 3) * k for k, v in list(d.items()) if v >= 2]

print(sum(arr) - max(temp + [0, 0]))

sys.stdout.flush()

