import math


def rints():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    (n, m) = rints()
    s = input()
    p = rints()
    occs = [0] * 26
    p.sort()
    ai = 0
    active = [1] * n
    rem = m + 1
    for pi in p:
        for i in range(ai, pi):
            active[i] = rem
        rem -= 1
        ai = pi
    for i in range(n):
        c = ord(s[i]) - ord('a')
        occs[c] += active[i]
    print(*occs)
