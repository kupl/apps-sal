N = int(input())
S = [input() + ".", input() + ","]
mod = 10**9 + 7

if N == 1:
    print(3)
    return

if S[0][0] == S[1][0]:
    i = 1
    ans = 3
else:
    i = 2
    ans = 6

while i < N:
    if S[0][i] == S[1][i]:
        if S[0][i - 1] == S[1][i - 1]:
            ans *= 2
        else:
            pass
        ans %= mod
        i += 1

    else:
        if S[0][i - 1] == S[1][i - 1]:
            ans *= 2
        else:
            ans *= 3
        ans %= mod
        i += 2

print(ans)
