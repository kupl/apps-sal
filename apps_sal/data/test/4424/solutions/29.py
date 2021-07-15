import sys
K, X = map(int, next(sys.stdin).split())
print('Yes' if K * 500 >= X else 'No')
