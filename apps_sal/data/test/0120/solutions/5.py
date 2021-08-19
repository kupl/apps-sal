n = int(input())
s = input()


def solve(n, s):
    if n % 4 > 0:
        return '==='
    for c in 'ACGT':
        if 4 * s.count(c) > n:
            return '==='
    r = ''
    for c in 'ACGT':
        r += c * (n // 4 - s.count(c))
    j = 0
    res = ''
    for c in s:
        if c == '?':
            res += r[j]
            j += 1
        else:
            res += c
    return res


print(solve(n, s))
