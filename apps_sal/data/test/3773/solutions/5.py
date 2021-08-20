import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def grundy(a, k):
    while 1:
        if a < k:
            return 0
        if a % k == 0:
            return a // k
        once = a // k + 1
        seg = a % k
        cnt = (seg + once - 1) // once
        a -= cnt * once


win = 0
for _ in range(II()):
    (a, k) = MI()
    win ^= grundy(a, k)
if win:
    print('Takahashi')
else:
    print('Aoki')
