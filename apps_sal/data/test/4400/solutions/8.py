s = input()
ans = 0
if "R" in s:
    if s[0] == s[1] or s[1] == s[2]:
        ans = s.count("R")
    else:
        ans += 1
print(ans)

