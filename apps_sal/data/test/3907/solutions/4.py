import sys
import bisect
(n, m), *s = [map(int, s.split()) for s in sys.stdin.readlines()]
g = [n * (n - 1) // 2 + (n - 1) % 2 * (n // 2 - 1) for n in range(1, 2002)]
print(sum(sorted([w for _, w in s], reverse=True)[:min(m, bisect.bisect_left(g, n))]))
