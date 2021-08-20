import sys
input = sys.stdin.readline
alpha = 'abcdefghijklmnopqrstuvwxyz'
count = {}
for i in alpha:
    count[i] = 0
(n, f) = list(map(int, input().split()))
balls = list(input().strip('\n'))
for i in range(n):
    count[balls[i]] += 1
max = 0
for i in alpha:
    if count[i] > max:
        max = count[i]
if max > f:
    print('NO')
else:
    print('YES')
