N = int(input())
S = input()

ans = [''] * N


def other(s):
    if s == 'S':
        return 'W'
    else:
        return 'S'


def calc(S):
    nonlocal ans
    for i, s in enumerate(S[1:], 1):
        if s == 'o':
            if ans[i] == 'S':
                ans[(i + 1) % N] = ans[i - 1]
            else:
                ans[(i + 1) % N] = other(ans[i - 1])
        else:
            if ans[i] == 'S':
                ans[(i + 1) % N] = other(ans[i - 1])
            else:
                ans[(i + 1) % N] = ans[i - 1]


if S[0] == 'o':
    ans[0] = 'S'
    ans[1] = 'S'
    calc(S)
    if (ans[0], ans[-1]) == ('S', 'S'):
        print(''.join(ans))
        return
    ans[0] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('W', 'W'):
        print(''.join(ans))
        return
    ans[0] = 'S'
    ans[1] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('S', 'W'):
        print(''.join(ans))
        return
    ans[0] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('W', 'S'):
        print(''.join(ans))
        return
else:
    ans[0] = 'S'
    ans[1] = 'S'
    calc(S)
    if (ans[0], ans[-1]) == ('S', 'W'):
        print(''.join(ans))
        return
    ans[0] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('W', 'S'):
        print(''.join(ans))
        return
    ans[0] = 'S'
    ans[1] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('S', 'S'):
        print(''.join(ans))
        return
    ans[0] = 'W'
    calc(S)
    if (ans[0], ans[-1]) == ('W', 'W'):
        print(''.join(ans))
        return

print(-1)
