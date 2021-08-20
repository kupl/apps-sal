s = input()
lis = []
for c in s:
    if c == 'B':
        if len(lis):
            lis = lis[:-1]
        else:
            continue
    else:
        lis.append(int(c))
for i in lis:
    print(i, end='')
print()
