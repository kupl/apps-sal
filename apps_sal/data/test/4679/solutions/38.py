s = {'a': input(), 'b': input(), 'c': input()}
now = 'a'
while s[now] != '':
    next = s[now][0]
    s[now] = s[now][1:]
    now = next
print(now.upper())
