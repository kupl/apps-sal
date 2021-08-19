import sys
input = sys.stdin.readline
n = int(input())
d = list(map(int, input().split()))
d.sort()
a = d[n // 2] - d[n // 2 - 1]
if a > 0:
    print(a)
else:
    print(0)
