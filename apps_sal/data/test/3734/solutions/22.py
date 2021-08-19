# ol = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
# dl = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2]
wl = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

a = wl.index(input())
b = wl.index(input())

if (b - a) % 7 in (0, 2, 3):
    print('YES')
else:
    print('NO')
