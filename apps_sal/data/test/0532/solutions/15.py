s = str(input())
s = s.strip()
res = 0
aord = ord('a')
for i in range(len(s)):
    t = abs(ord(s[i]) - aord)
    aord = ord(s[i])
    res = res + min(t, 26 - t)
print(res)
