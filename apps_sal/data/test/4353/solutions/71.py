s = list(input())
for i in s:
    if i == ',':
        print(" ", end='')
    else:
        print(i, end='')
