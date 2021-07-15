s = input()
res = set()
for i in range(len(s)):
    res.add(s[i:] + s[:i])
print(len(res))
