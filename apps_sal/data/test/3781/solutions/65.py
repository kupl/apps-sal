import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    if N % 2 == 1:
        print('Second')
        continue
    else:
        flg = True
        for i in range(N // 2):
            flg = flg & (A.pop() == A.pop())
        if flg:
            print('Second')
        else:
            print('First')
