import sys
(n, c) = [i for i in sys.stdin.read().strip().split('\n')]
n = int(n)
c = [int(i) for i in c.split()]
print(max(max(c) - 25, 0))
