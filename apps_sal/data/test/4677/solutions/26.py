n = []
for i in input():
    if i == 'B':
        if n: n.pop()
    else:
        n.append(i)
print(*n, sep='')
