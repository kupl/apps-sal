s = input()
res = 1
ans = -10000
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        res += 1
    else:
        ans = max(ans, res)
        res = 1
ans = max(ans, res)
res1 = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        res1 += 1
    else:
        break
res2 = 1
for i in range(len(s) - 2, res1 - 1, -1):
    if s[i] != s[i + 1]:
        res2 += 1
    else:
        break
if len(s) == 1:
    print(1)
elif s[0] == s[-1] or res1 + res2 > len(s):
    print(ans)
else:
    print(max(ans, res1 + res2))
