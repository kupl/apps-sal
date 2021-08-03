s = input()
s = s + "*"
ans = "Good"
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        ans = "Bad"
        break
print(ans)
