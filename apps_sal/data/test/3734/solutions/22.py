wl = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
a = wl.index(input())
b = wl.index(input())
if (b - a) % 7 in (0, 2, 3):
    print('YES')
else:
    print('NO')
