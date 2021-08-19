Mod = 1000000007
s = input()
n = len(s)
(a, b, c, d) = (1, 0, 0, 0)
for i in range(0, n):
    if s[i] == '*':
        t = (0, a + b + d, 0, 0)
    elif s[i] == '?':
        t = (a + b + c, a + b + d, 0, 0)
    elif s[i] == '0':
        t = (0, 0, a + c, 0)
    elif s[i] == '1':
        t = (0, 0, b, a + c)
    else:
        t = (0, 0, 0, b + d)
    (a, b, c, d) = [a % Mod for a in t]
print((a + b + c) % Mod)
