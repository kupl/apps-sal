s = input()
t = ''
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'b':
        t += s[i]
boo = False
t += 'b'
ans = 1
cur = 0
for i in range(len(t)):
    if boo:
        if t[i] == 'a':
            cur += 1
        else:
            ans *= cur
            ans %= 1000000007
            boo = False
    else:
        if t[i] == 'a':
            cur = 2
            boo = True
print((ans - 1) % 1000000007)
