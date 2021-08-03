s = input()
e = s
ss = set()
for i in range(len(s)):
    e = e[-1] + e[:-1]
    ss.add(e)
print(len(ss))
