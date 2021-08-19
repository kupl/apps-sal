s = [input() for i in range(3)]
t = ['a', 'b', 'c']
cur = 0
while len(s[cur]) > 0:
    next = s[cur][0]
    s[cur] = s[cur][1:]
    cur = t.index(next)
print(t[cur].upper())
