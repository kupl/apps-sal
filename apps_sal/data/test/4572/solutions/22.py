s = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

for x in alphabets:
    if x in s:
        continue
    else:
        print(x)
        break
else:
    print('None')
