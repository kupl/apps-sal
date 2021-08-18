

n = int(input())
mod = 10 ** 9 + 7
s = [list(input()) for _ in range(2)]
ans = 1
i = 0
while i < n:
    if s[1][i] == s[0][i]:
        if i == 0:
            ans *= 3
            i += 1
        else:
            if s[0][i - 1] == s[1][i - 1]:
                ans = (ans * 2) % mod
            i += 1
    else:
        if i == 0:
            ans *= 6
        else:
            if s[0][i - 1] == s[1][i - 1]:
                ans = (ans * 2) % mod
            else:
                ans = (ans * 3) % mod
        i += 2


print(ans)
