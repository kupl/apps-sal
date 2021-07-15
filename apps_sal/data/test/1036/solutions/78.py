def winner(x, y):
    return x if x + y in ['RS', 'PR', 'SP'] else y

def f(level, offset):
    if (level, offset) in memo:
        return memo[level, offset]
    if level == 0:
        ret = s[offset]
    else:
        sub1 = f(level - 1, offset)
        sub2 = f(level - 1, (offset + 2 ** (level - 1)) % n)
        ret = winner(sub1, sub2)
    memo[level, offset] = ret
    return ret

n, k = list(map(int, input().split()))
s = input()

memo = {}
print((f(k, 0)))

