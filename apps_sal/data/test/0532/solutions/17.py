s = input()
b = 'abcdefghijklmnopqrstuvwxyz'
c = 0
now = 0
for i in range(len(s)):
    need = b.find(s[i])
    c += min(abs(now - need), abs(26 - abs(now - need)))
    now = need
print(c)
