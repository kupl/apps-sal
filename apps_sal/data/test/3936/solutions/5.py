n = int(input())
s1 = input()
s2 = input()
ans = 1
i = 1
mod = 1000000007
if s1[0] == s2[0]:
    ans = 3
    i = 1
else:
    ans = 6
    i = 2
while i < n:
    if s1[i - 1] == s2[i - 1]:
        if s1[i] == s2[i]:
            ans = (ans * 2) % mod
            i += 1
            continue
        else:
            ans = (ans * 2) % mod
            i += 2
            continue
    else:
        if s1[i] == s2[i]:
            ans = (ans * 1) % mod
            i += 1
            continue
        else:
            ans = (ans * 3) % mod
            i += 2
            continue
print(ans)
