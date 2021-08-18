def get_num(sym):
    if sym in '0123456789':
        return int(sym)
    if sym == '-':
        return 62
    if sym == '_':
        return 63
    if ord('a') <= ord(sym) <= ord('z'):
        return ord(sym) - ord('a') + 36
    else:
        return ord(sym) - ord('A') + 10


def bins(x):
    return bin(x)[2:]


p = 10**9 + 7
s = input()
ans = 1
for sym in s:
    now = bins(get_num(sym))
    now = '0' * (6 - len(now)) + now
    for i in now:
        if i is '0':
            ans *= 3
    ans %= p

print(ans)
