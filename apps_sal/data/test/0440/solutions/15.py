n = input()
s = input()
v = 'euoaiy'
i = 1
while True:
    if i >= len(s):
        break
    if s[i] in v and s[i - 1] in v:
        s = s[:i] + s[i + 1:]
    else:
        i += 1
print(s)
