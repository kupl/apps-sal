import sys
3


n, m = list(map(int, sys.stdin.readline().strip().split()))
pieces = list(map(int, sys.stdin.readline().strip().split()))
pieces.sort()

diff = []

for i in range(0, m - n + 1):
    diff.append(pieces[i + n - 1] - pieces[i])

print(min(diff))
