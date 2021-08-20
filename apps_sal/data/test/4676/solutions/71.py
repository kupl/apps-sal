s = input()
t = input()
ans = ''
if (len(s) + len(t)) % 2 == 0:
    for i in range(len(s)):
        ans += s[i]
        ans += t[i]
else:
    for i in range(len(t)):
        ans += s[i]
        ans += t[i]
    ans += s[-1]
print(ans)
