s = input()
mod = 1e9 + 7

ans = 1
cnt = 0
for i in range(len(s)):
    if s[i] != 'b':
        if s[i] == 'a':
            cnt += 1
    else:
        if cnt > 0:
            ans = (ans * (cnt + 1)) % mod
        cnt = 0

if cnt > 0:
    ans = (ans * (cnt + 1)) % mod

print(int(ans) - 1)
