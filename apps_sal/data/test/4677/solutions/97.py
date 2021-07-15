s = input()
ans = ""
for _ in range(len(s)):
    if s[0] == "0":
        ans += "0"
        s = s[1:]
    elif s[0] == "1":
        ans += "1"
        s = s[1:]
    else:
        s = s[1:]
        ans = ans[:-1]
print(ans)
