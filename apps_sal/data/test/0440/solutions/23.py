n = int(input())
w = ['a', 'e', 'i', 'o', 'u', 'y']
res = []
for c in input():
    if len(res) == 0:
        res.append(c)
        continue
    if c in w:
        if res[-1] in w:
            continue
    res.append(c)
print(''.join(res))
