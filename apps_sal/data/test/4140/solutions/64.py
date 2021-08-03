s = input()

if s[0] == "1":
    ans = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != "1":
            ans += 1
        elif i % 2 == 1 and s[i] != "0":
            ans += 1
else:
    ans = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != "0":
            ans += 1
        elif i % 2 == 1 and s[i] != "1":
            ans += 1
print(ans)
