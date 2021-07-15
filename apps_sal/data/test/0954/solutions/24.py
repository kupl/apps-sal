s = input()
a = set()
for i in range(len(s)):
    a.add(s[i:] + s[:i])
print(len(a))
