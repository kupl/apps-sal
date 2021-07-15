s = input()
mn = 1000
for elem in s:
    if mn < ord(elem):
        print('Ann')
    else:
        print('Mike')
        mn = ord(elem)

