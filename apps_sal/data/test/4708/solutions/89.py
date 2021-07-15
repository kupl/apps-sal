import sys
N, K, X, Y = map(int, sys.stdin.readlines())
print(N*X if N <= K else K*X +Y*(N-K))
