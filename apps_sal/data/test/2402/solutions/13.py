import sys
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
t = int(input())
for _ in range(t):
    (n, x, y) = list(map(int, input().split()))
    below1 = max(n - x - (y - 1), 0)
    below2 = max(n - y - (x - 1), 0)
    worst = n - max(below1, below2)
    above1 = min(max(x - 1 - (n - y - 1), 0), n - 1)
    above2 = min(max(y - 1 - (n - x - 1), 0), n - 1)
    best = max(above1, above2) + 1
    print(best, worst)
