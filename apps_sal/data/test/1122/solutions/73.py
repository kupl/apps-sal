#from collections import deque,defaultdict
printn = lambda x: print(x, end='')
inn = lambda: int(input())
inl = lambda: list(map(int, input().split()))
inm = lambda: map(int, input().split())
ins = lambda: input().strip()
DBG = True  # and False
BIG = 10**18
R = 10**9 + 7


def ddprint(x):
    if DBG:
        print(x)


n, m = inm()
if n % 2 == 1:
    for i in range(1, m + 1):
        print('{} {}'.format(i, n - i))
elif n % 4 == 0:
    e = min(m + 1, n // 4)
    for i in range(1, e):
        print('{} {}'.format(i, n // 2 - i))
    if m >= n // 4:
        for i in range(m - n // 4 + 1):
            print('{} {}'.format(n - 1 - i, n // 2 + i))
else:
    e = min(m + 1, n // 4 + 1)
    for i in range(1, e):
        print('{} {}'.format(i, n // 2 - i + 1))
    if m >= n // 4 + 1:
        for i in range(m - n // 4):
            print('{} {}'.format(n - 1 - i, n // 2 + i + 1))
