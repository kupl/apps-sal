from collections import defaultdict
n = int(input())
s1 = input()
s2 = input()
ans = 0
mod = 10 ** 9 + 7
if s1[0] == s2[0]:
    i = 1
    ans += 3
    flag = False
else:
    i = 2
    ans += 6
    flag = True
while i < n:
    if flag:
        if s1[i] == s2[i]:
            flag = False
        else:
            ans *= 3 % mod
            i += 1
    else:
        ans *= 2 % mod
        if s1[i] != s2[i]:
            flag = True
            i += 1
    i += 1
print(ans % mod)
