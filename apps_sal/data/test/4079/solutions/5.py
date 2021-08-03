mod = 10 ** 9 + 7
def ii(): return int(input())
def si(): return input()
def dgl(): return list(map(int, input()))
def f(): return map(int, input().split())
def il(): return list(map(int, input().split()))
def ls(): return list(input())


n = ii()
for i in range(n):
    s = sorted(list(si()))
    x = len(s)
    flg = 0
    for j in range(1, x):
        if ord(s[j]) - ord(s[j - 1]) != 1:
            flg = 1
    print('YNeos'[flg == 1::2])
