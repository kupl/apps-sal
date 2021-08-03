import sys
mod = 1000000007
n = int(input())
s1 = input()
s2 = input()
flag1 = 0
flag2 = 0
for i in range(n):
    if s1[i] != "?" and s2[i] != "?" and s1[i] > s2[i]:
        flag1 = 1
    if s1[i] != "?" and s2[i] != "?" and s1[i] < s2[i]:
        flag2 = 1
if flag1 and flag2:
    ans = 1
    for i in range(n):
        if s1[i] == "?":
            ans *= 10
            ans %= mod
    for i in range(n):
        if s2[i] == "?":
            ans *= 10
            ans %= mod
    print(ans % mod)
    return
if not(flag1) and not(flag2):
    ans1 = 1
    ans2 = 1
    x = 0
    al = 1
    for i in range(n):
        if s1[i] == "?" and s2[i] == "?":
            x += 1
    for i in range(n):
        if s1[i] == "?":
            al *= 10
            al %= mod
    for i in range(n):
        if s2[i] == "?":
            al *= 10
            al %= mod
    for i in range(n):
        if s1[i] == "?" and s2[i] == "?":
            ans1 *= 55
            ans1 %= mod
        elif s1[i] == "?":
            ans1 *= 10 - int(s2[i])
            ans1 %= mod
        elif s2[i] == "?":
            ans1 *= int(s1[i]) + 1
            ans1 %= mod
    s1, s2 = s2, s1
    for i in range(n):
        if s1[i] == "?" and s2[i] == "?":
            ans2 *= 55
            ans2 %= mod
        elif s1[i] == "?":
            ans2 *= 10 - int(s2[i])
            ans2 %= mod
        elif s2[i] == "?":
            ans2 *= int(s1[i]) + 1
            ans2 %= mod
    y = 1
    for i in range(x):
        y *= 10
        y %= mod
    print((al - (ans1 + ans2 - y)) % mod)
    return
if flag2:
    s1, s2 = s2, s1
ans = 1
al = 1
for i in range(n):
    if s1[i] == "?":
        al *= 10
        al %= mod
for i in range(n):
    if s2[i] == "?":
        al *= 10
        al %= mod
for i in range(n):
    if s1[i] == "?" and s2[i] == "?":
        ans *= 55
        ans %= mod
    elif s1[i] == "?":
        ans *= 10 - int(s2[i])
        ans %= mod
    elif s2[i] == "?":
        ans *= int(s1[i]) + 1
        ans %= mod
print((al - ans) % mod)
