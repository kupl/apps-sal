n = int(input())
s = list(input())
ans = ""
for i in range(len(s)):
    s[i] = ord(s[i]) + n
    if s[i] >= 91:
        s[i] -= 26
    ans += chr(s[i])
print(ans)
