import sys


def input():
    return sys.stdin.readline().rstrip()


K = int(input())
(A, B) = map(int, input().split())
ans = False
count = K
while count <= B:
    if A <= count and count <= B:
        ans = True
    count += K
if ans:
    print('OK')
else:
    print('NG')
