N = int(input())
S = [input() for i in range(2)]
MOD = 1000000007

ans = 1
prev = ''
i = 0
while i < N:
    if S[0][i] == S[1][i]:
        if prev == '|':
            ans *= 2
        elif prev == '-':
            ans *= 1
        else:
            ans *= 3
        prev = '|'
        i += 1
    else:
        if prev == '|':
            ans *= 2
        elif prev == '-':
            ans *= 3
        else:
            ans *= 6
        prev = '-'
        i += 2

    ans %= MOD

print(ans)
