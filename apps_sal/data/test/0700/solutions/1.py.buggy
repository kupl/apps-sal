N = int(input())
s1 = [list(input()) for i in range(N)]
s2 = [list(input()) for i in range(N)]


def rotate(s):
    ret = [[None for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = s[j][N - 1 - i]
    return ret


def v_mirror(s):
    return list(reversed(s))


def h_mirror(s):
    return [list(reversed(row)) for row in s]


def solve():
    nonlocal s1
    for i in range(4):
        if s1 == s2:
            return True
        if v_mirror(s1) == s2:
            return True
        if h_mirror(s1) == s2:
            return True
        if v_mirror(h_mirror(s1)) == s2:
            return True
        s1 = rotate(s1)
    return False


print('Yes' if solve() else 'No')
