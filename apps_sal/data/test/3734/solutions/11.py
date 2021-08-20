s1 = input()
s2 = input()
n1 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(s1)
n2 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(s2)
if n1 == n2:
    print('YES')
elif (n2 - n1 + 7) % 7 in [2, 3]:
    print('YES')
else:
    print('NO')
