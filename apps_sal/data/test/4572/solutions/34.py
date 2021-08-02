import string

s = input()
for x in string.ascii_lowercase:
    if x not in s:
        print(x)
        break
else:
    print('None')
