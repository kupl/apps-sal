input()
s = input()
z = []
prev = ''
for el in s:
    if el == 'R':
        if prev == 'U':
            prev = ''
            z[-1] = 'D'
        else:
            z.append(el)
            prev = 'R'
    elif prev == 'R':
        prev = ''
        z[-1] = 'D'
    else:
        z.append(el)
        prev = 'U'
print(len(z))
