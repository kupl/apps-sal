s = input()
l = []
for i in s:
    if i in l:
        print('no')
        return
    else:
        l.append(i)
print('yes')
