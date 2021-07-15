input()
s = input()

res = []
counter = 0

for c in s:
    if c == 'B':
        counter += 1
    elif c == 'W':
        if counter > 0:
            res.append(counter)
        counter = 0

if counter > 0:
    res.append(counter)

print(len(res))
for r in res:
    print(r, end=' ')
print()

