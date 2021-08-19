import sys
3
(n, A) = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
s = sum(d)
for x in d:
    z = min(A - n + 1, x) - max(1, A - s + x) + 1
    if z < 0:
        z = 0
    sys.stdout.write('%d ' % (x - z))
sys.stdout.write('\n')
