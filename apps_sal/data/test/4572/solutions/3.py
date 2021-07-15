import string

S = set(input())

result = ''
for i in string.ascii_lowercase:
    if i not in S:
        print(i)
        break
else:
    print('None')
