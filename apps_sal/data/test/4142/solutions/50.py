s = input()
ans = "Yes"
for i in range(len(s)):
    if (i + 1) % 2 == 1:
        if s[i] == "L":
            ans = "No"
    else:
        if s[i] == "R":
            ans = "No"
print(ans)
