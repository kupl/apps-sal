a = input()
b = []
l = 0
for i in range(len(a)):
    if a[i] != 'a' and a[i] != 'e' and a[i] != 'i' and a[i] != 'o' and a[i] != 'u':
        if l < 2:
            l += 1
        else:
            if a[i] != a[i - 1] or a[i] != a[i - 2]:
                l = 1
                b.append(' ')
    else:
        l = 0
    b.append(a[i])
print(''.join(map(str, b)))
