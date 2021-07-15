n = int(input())
a = []

for x in range(n) : a.append(str(input()))
for x in range(n):
    if (a[x][-5:] == 'lala.' and a[x][:5] == 'miao.'): print('OMG>.< I don\'t know!')
    elif (a[x][-5:] == 'lala.'): print('Freda\'s')
    elif (a[x][:5] == 'miao.'): print('Rainbow\'s')
    else: print('OMG>.< I don\'t know!')
