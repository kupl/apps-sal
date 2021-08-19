n = int(input())
s = list(input())
a = []
b = 0
for i in s:
    a.append(i)
    b += 1
    if b > 2:
        if a[-3:] == ['f', 'o', 'x']:
            del a[-3:]
            b -= 3
print(b)
