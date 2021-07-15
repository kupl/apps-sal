days = [28, 30, 31]
week = ['monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday']

a = input()
b = input()

for index, name in enumerate(week):
    if name == a:
        ind = index

flag = False
for mo in days:
    if week[(ind + mo) % 7] == b:
        flag = True
if flag:
    print('YES')
else:
    print('NO')

