import sys
(N, A) = map(int, sys.stdin.readlines())
N %= 500
print('Yes' if N <= A else 'No')
