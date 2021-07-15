import sys

def dbg(*args):
    print('D:', *args, file=sys.stderr)

n, p = map(int, input().split())
s = input()

if s == s[::-1]:
    print('0')
else:
    sz = len(s)
    if p > sz//2:
        p = sz - p
    else:
        p -= 1

    l, r = 0, sz//2 - 1
    while s[l] == s[-l - 1]: l += 1
    while s[r] == s[-r - 1]: r -= 1
    dbg(l, r, p)
    sum = r - l
    sum += min(abs(p - l), abs(r - p))
    for i in range(l, r + 1):
        a1 = ord(s[i])
        a2 = ord(s[-i - 1])
        if (a1 > a2):
            a1, a2 = a2, a1
        sum += min(a2 - a1, a1 + 26 - a2)
    print(sum)
