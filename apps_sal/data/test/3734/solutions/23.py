d = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}
first = d[input()]
second = d[input()]
cnt = (second + 7 - first) % 7
s = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30}
for v in s:
    if v % 7 == cnt:
        print('YES')
        break
else:
    print('NO')
