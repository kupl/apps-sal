s = input()
ans = 1
for i in range(len(s)):
    if (i + 1) & 1:
        if s[i] not in "RUD":
            ans = 0
    else:
        if s[i] not in "LUD":
            ans = 0
print("Yes" if ans == 1 else "No")
