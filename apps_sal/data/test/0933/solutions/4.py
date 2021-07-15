s = input()
s1 = list(s[:2])
for i in range(2,len(s)):
    if not(s[i] == s[i-1] == s[i-2]):
        s1.append(s[i])
ans = s1[:3]
if len(ans) >= 3:
    for i in range(3, len(s1)):
        if not(s1[i] == s1[i-1] and s1[i-2] == s1[i-3]):
            ans += s1[i]
        else:
            s1[i] = '!'
for i in range(len(ans)):
    print(ans[i], end = '')
