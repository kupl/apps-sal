import sys

def solve():
    s = input()

    if is_subst(s, 'heidi'):
        print('YES')
    else:
        print('NO')

def is_subst(s, t):
    tlen = len(t)
    slen = len(s)
    cnt = 0

    l = 0

    for i in range(tlen):
        for j in range(l, slen):
            if t[i] == s[j]:
                l = j + 1
                cnt += 1
                break
        else:
            l = slen

    return cnt == tlen

def __starting_point():
    solve()
__starting_point()
