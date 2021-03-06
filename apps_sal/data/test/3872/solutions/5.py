def read_list(t):
    return [t(x) for x in input().split()]


def read_line(t):
    return t(input())


def read_lines(t, N):
    return [t(input()) for _ in range(N)]


def smallest(s):
    len_s = len(s)
    if len_s & 1:
        return s
    s1 = smallest(s[:len_s // 2])
    s2 = smallest(s[len_s // 2:])
    return s1 + s2 if s1 < s2 else s2 + s1


S1 = read_line(str)
S2 = read_line(str)
print('YES' if smallest(S1) == smallest(S2) else 'NO')
