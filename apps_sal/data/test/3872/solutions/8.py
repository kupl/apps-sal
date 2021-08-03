def g(s):
    l = len(s)
    return sorted([g(s[:l // 2]), g(s[l // 2:])])if l % 2 == 0 else s


print('YES'if g(input()) == g(input())else'NO')
