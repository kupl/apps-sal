import sys
readline = sys.stdin.readline
(D, T, S) = map(int, readline().split())
print(('No', 'Yes')[S * T >= D])
