a = input()
x = 2
while x < len(a):
    if a[x] != 'a' and a[x] != 'e' and (a[x] != 'i') and (a[x] != 'o') and (a[x] != 'u') and (a[x] != ' '):
        if a[x - 1] != 'a' and a[x - 1] != 'e' and (a[x - 1] != 'i') and (a[x - 1] != 'o') and (a[x - 1] != 'u') and (a[x - 1] != ' ') and (a[x - 2] != 'a') and (a[x - 2] != 'e') and (a[x - 2] != 'i') and (a[x - 2] != 'o') and (a[x - 2] != 'u') and (a[x - 2] != ' '):
            if a[x - 2] != a[x] or a[x] != a[x - 1]:
                a = a[0:x] + ' ' + a[x:]
                x += 1
    x += 1
print(a)
