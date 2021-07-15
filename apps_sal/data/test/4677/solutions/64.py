s = input()
a = []
for c in s:
    if c in ['0', '1']:
        a.append(c)
    else:
        if len(a) != 0:
            a.pop()
print(''.join(a))
