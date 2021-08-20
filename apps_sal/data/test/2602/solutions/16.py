import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (a, b, n, m) = map(int, input().split())
    if a + b < n + m:
        print('No')
        continue
    if min(a, b) < m:
        print('No')
    else:
        print('Yes')
