import sys
f = sys.stdin
n = int(f.readline())
a = list(map(int, f.readline().split()))
print(max(sum(a[:i]) + sum(1 - t for t in a[i:j + 1]) + sum(a[j + 1:]) for i in range(n) for j in range(i, n)))
