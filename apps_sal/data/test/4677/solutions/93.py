a = input()
b = ''
for elem in a:
    if elem == '1':
        b += '1'
    elif elem == '0':
        b += '0'
    else:
        b = b[:-1]
print(b)
