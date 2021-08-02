import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def solve():
    s = [ord(i) - ord('a') for i in minp()]
    c = [False] * 26
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if (j - i) % 2 == 1:
            c[s[i]] = True
        i = j
    for i in range(26):
        if c[i]:
            print(chr(i + ord('a')), end='')
    print()


for i in range(mint()):
    solve()
