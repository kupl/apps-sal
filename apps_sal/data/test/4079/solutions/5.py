mod = 10 ** 9 + 7
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
n = ii()
for i in range(n):
    s = sorted(list(si()))
    x = len(s)
    flg = 0
    for j in range(1, x):
        if ord(s[j]) - ord(s[j - 1]) != 1:
            flg = 1
    print('YNeos'[flg == 1::2])
