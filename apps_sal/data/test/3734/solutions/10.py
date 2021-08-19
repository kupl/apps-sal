ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = dict(list(zip(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], list(range(7)))))
(a, b) = (d[input()], d[input()])
good = False
for i in range(11):
    if (a + ms[i]) % 7 == b:
        good = True
print('YES' if good else 'NO')
