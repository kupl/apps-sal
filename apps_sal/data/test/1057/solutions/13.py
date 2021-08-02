n = int(input())
s = input()
MOD = 998244353
left = 0
right = 0
right_1 = 0
a, b, c = True, True, True
i = 0
while (a or b or c) and i < n:
    if a and s[i] == s[0]:
        left += 1
    else:
        a = False
    if b and s[-i - 1] == s[0]:
        right += 1
    else:
        b = False
    if c and s[-i - 1] == s[-1]:
        right_1 += 1
    else:
        c = False
    i += 1
if right != 0:
    print((1 + left * right + left + right) % MOD)
else:
    print((1 + left + right_1) % MOD)
