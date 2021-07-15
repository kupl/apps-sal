t = input()
t = t.replace('heavy', '0')
t = t.replace('metal', '1')

a, b, s = 0, t.count('1'), 0
for i in t:
    if i == '0':
        a += 1
        s += b
    elif i == '1': b -= 1
print(s)
