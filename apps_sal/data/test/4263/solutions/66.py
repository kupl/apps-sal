s = input()
ans = 0
tmp = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] == "A" or s[j] == "C" or s[j] == "G" or s[j] == "T":
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
            break
    else:
        ans = max(ans, tmp)
        tmp = 0
print(ans)
