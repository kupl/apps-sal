from sys import stdin
(n, s) = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
if sum(arr) - max(arr) > s:
    print('NO')
else:
    print('YES')
