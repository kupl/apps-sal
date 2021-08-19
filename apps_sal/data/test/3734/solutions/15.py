m = [3, 0, 2]
a = input()
b = input()
month = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if (month.index(b) - month.index(a)) % 7 in m:
    print('YES')
else:
    print('NO')
