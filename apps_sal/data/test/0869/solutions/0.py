import sys


n, m = [int(i) for i in input().split()]
first = min(n, m)
second = (max(n, m) - first) // 2
print(first, second)
