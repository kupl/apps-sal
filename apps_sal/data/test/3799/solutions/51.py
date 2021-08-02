s = (input())
l = len(s)
e = (s[0] == s[-1])
print(("First" if (e + l) % 2 else "Second"))
