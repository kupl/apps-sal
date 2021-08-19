S = list(input())
T = list(input())


def match(s, t):
    for (_s, _t) in zip(s, t):
        if not (_s == _t or _s == '?'):
            return False
    return True


def convert(S):
    for i in range(len(S)):
        if S[i] == '?':
            S[i] = 'a'
    return S


def replace(S, T, off):
    for i in range(len(T)):
        S[off + i] = T[i]
    return S


pos = -1
for i in reversed(range(0, len(S) - len(T) + 1)):
    if match(S[i:], T):
        pos = i
        break
if 0 <= pos:
    ans = S
    ans = replace(ans, T, pos)
    ans = convert(ans)
    print(*ans, sep='')
else:
    print('UNRESTORABLE')
