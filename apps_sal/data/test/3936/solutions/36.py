n = int(input())
s = [input() for _ in range(2)]
mod = 10 ** 9 + 7
if s[0][0] == s[1][0]:
    ans = 3
    i = 1
    l = 1
else:
    ans = 6
    i = 2
    l = 0
while i < n:
    if s[0][i] == s[1][i]:
        if l == 1:
            ans *= 2
        l = 1
        i += 1
    else:
        if l == 1:
            ans *= 2
        else:
            ans *= 3
        l = 0
        i += 2
    ans %= mod
print(ans)
