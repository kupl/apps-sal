n = int(input())
S = [list(input()) for _ in range(2)]
mod = 1000000007
if S[0][0] == S[1][0]:
    ans = 3
    i = 1
    typ = '2x1'
else:
    ans = 6
    i = 2
    typ = '2x2'
while i < n:
    if S[0][i] == S[1][i]:
        if typ == '2x1':
            ans *= 2
        typ = '2x1'
        i += 1
    else:
        if typ == '2x1':
            ans *= 2
        else:
            ans *= 3
        typ = '2x2'
        i += 2
    ans %= mod
print(ans)
