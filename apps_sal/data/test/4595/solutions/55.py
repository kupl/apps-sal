a = input()
b = a[::-1]
p = 0

for i in range(len(a)):
    if a[0] != 'A':
        a = a[1:]
    else:
        break

for i in range(len(a)):
    if a[-1] != 'Z':
        a = a[:-1]
    else:
        break


print(len(a))
