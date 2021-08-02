s = "A" + input() + "A"
ans = 0
prev = -1
for i in range(len(s)):
    if (s[i] in "AEIOUY"):
        ans = max(ans, i - prev)
        prev = i
print(ans)
