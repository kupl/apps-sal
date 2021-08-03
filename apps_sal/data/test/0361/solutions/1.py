s = input()
ss = "CODEFORCES"
ans = "NO"
for i in range(len(s)):
    for j in range(i, len(s)):
        h = s[0:i] + s[j + 1:]
        if (h == ss):
            ans = "YES"
print(ans)
