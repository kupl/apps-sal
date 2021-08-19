__author__ = 'Andrey'
(k, n, w) = map(int, input().split())
needed = w * (w + 1) // 2 * k
if needed <= n:
    print(0)
else:
    print(needed - n)
