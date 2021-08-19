s = input()
known = set()
for i in range(len(s)):
    p = s[i:] + s[:i]
    known.add(p)
print(len(known))
