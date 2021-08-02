n = int(input())
s = input()
t = input()
mod = 10**9 + 7
ans = 1
if s[0] == t[0]:
    ans *= 3
    idx = 1
    flag = 0
else:
    ans *= 6
    idx = 2
    flag = 1
while idx < n:
    if s[idx] == t[idx]:
        if flag:
            idx += 1

        else:
            ans = ans * 2 % mod
            idx += 1
        flag = 0
    else:
        if flag:
            ans = ans * 3 % mod
        else:
            ans = ans * 2 % mod
        idx += 2
        flag = 1

print(ans)
