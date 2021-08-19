import sys
(n, a, b) = map(int, sys.stdin.readline().split())
w_arr = map(int, sys.stdin.readline().split())
print(' '.join(map(str, [w * a % b // a for w in w_arr])))
