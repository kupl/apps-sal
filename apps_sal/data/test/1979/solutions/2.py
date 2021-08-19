from collections import Counter
from sys import stdin
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {j: i for (i, j) in enumerate(b)}
ds = []
for i in range(n):
    ds.append((d[a[i]] - i) % n)
print(max(Counter(ds).values()))
