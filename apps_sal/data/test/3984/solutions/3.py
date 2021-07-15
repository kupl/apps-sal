s = input()
mi = 'z'
for x in s:
    if x > mi:
        print('Ann')
    else:
        print('Mike')
    mi = min(x, mi)

