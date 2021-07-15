n = int(input())
a = input()

dic = {'SF': 0, 'FS': 0}

for i in range(1, n):
    if a[i - 1] == 'F' and a[i] == 'S':
        dic['FS'] += 1
    elif a[i - 1] == 'S' and a[i] == 'F':
        dic['SF'] += 1
if dic['SF'] > dic['FS']:
    print('YES')
else:
    print('NO')
