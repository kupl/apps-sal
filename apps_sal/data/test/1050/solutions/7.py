from sys import stdin
input = stdin.readline
(n, m, k) = list(map(int, input().split()))
if min(m, k) >= n:
    print('Yes')
else:
    print('No')
