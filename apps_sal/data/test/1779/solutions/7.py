s = input()
t = input()

l = {}

for i in range(26):
    l[s[i]] = ord(t[i]) - ord(s[i])

ans = ''

for c in input():
    ans += chr(ord(c) + l.get(c.lower(), 0))

print(ans)
