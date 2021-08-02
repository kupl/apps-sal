import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))

i = 0
while (sum(l) + k * i) / (i + n) < k - 0.5:
    i += 1

sys.stdout.write(str(i))
