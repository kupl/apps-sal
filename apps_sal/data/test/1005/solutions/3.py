from math import inf
for _ in range(int(input())):
    n, k, d = list(map(int, input().split()))
    data = tuple(map(int, input().split()))
    best = inf
    for i in range(n - d + 1):
        best = min(best, len(set(data[i:i + d])))
    print(best)
