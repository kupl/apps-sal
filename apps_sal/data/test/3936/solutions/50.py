n = int(input())
s1 = input()
s2 = input()

ans = 1
mod = 10 ** 9 + 7

tmp = 3
i = 0
f = -1

while i < n:
    if s1[i] == s2[i]:
        if f == 1:
            tmp = 1
        elif f == 0:
            tmp = 2
        ans *= tmp
        ans %= mod
        f = 0
    else:
        if f == 1:
            tmp = 3
        elif f == 0:
            tmp = 2
        else:
            tmp = 6
        ans *= tmp
        ans %= mod
        i += 1
        f = 1
    i += 1

print(ans)
