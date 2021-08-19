s = input().rstrip()
minimum = 'z'
for ch in s:
    if ch > minimum:
        print('Ann')
    else:
        print('Mike')
        minimum = ch
