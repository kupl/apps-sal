import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
s = sum(l)
if s % 2 == 1:
    print('NO')
elif max(l) > s // 2:
    print('NO')
else:
    print('YES')
