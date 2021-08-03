from collections import Counter


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, k = mi()
s = input().strip()
c = Counter(s)
mn = 10 ** 9
for ch in alpha[:k]:
    mn = min(mn, c[ch])
print(mn * k)
