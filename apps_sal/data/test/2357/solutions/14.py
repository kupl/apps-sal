from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    prev = Counter()
    mn = n + 1
    for i, el in enumerate(a):
        if el in prev:
            mn = min(mn, i - prev[el] + 1)
        prev[el] = i
    print(mn if mn < n + 1 else -1)
