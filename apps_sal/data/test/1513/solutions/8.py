(n, m, k) = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
diffs = [b[i + 1] - b[i] - 1 for i in range(len(b) - 1)]
diffs.sort()
print(n + sum(diffs[:n - k]))
