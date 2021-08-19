s = input()
color = s[0]
result = 0
for i in range(len(s)):
    if color != s[i]:
        result += 1
        color = s[i]
print(result)
