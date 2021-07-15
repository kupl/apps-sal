alpha = list('abcdefghijklmnopqrstuvwxyz')
s = input()
for i in alpha:
    if not i in s:
        print(i)
        return
print('None')
