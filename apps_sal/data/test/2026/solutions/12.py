n = int(input())
s = input()
ans = 1
rl = ''
ud = ''
for i in range(n):
    if s[i] == 'L' or s[i] == 'R':
        if not rl:
            rl = s[i]
        elif rl != s[i]:
            ans += 1
            rl, ud = s[i], 0
    elif s[i] == 'U' or s[i] == 'D':
        if not ud:
            ud = s[i]
        elif ud != s[i]:
            ans += 1
            rl, ud = 0, s[i]
print(ans)
