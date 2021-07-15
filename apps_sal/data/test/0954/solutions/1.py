s = input()
res = set()
for i in range(100):
    res.add(s)
    s = s[-1] + s[:-1]
print(len(res))
