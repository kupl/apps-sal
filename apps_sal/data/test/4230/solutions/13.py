import sys
input = iter(sys.stdin.read().splitlines()).__next__
sys.setrecursionlimit(10000)
(X, N) = list(map(int, input().split()))
S = set(map(int, input().split()))
bestr = 0
for r in range(0, 102):
    if r not in S:
        if abs(r - X) < abs(bestr - X):
            bestr = r
print(bestr)
