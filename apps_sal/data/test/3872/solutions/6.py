def g(s):
    l = len(s)
    return s if l % 2 == 1 else sorted([g(s[:l // 2]), g(s[l // 2:])])


print('YES'if g(input()) == g(input())else'NO')
