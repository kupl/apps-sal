a = input()
h = int(a[0:2])
m = int(a[3:5])
n = int(input())
per = (m + n) // 60
m = (m + n) % 60
h = (h + per) % 24
if h < 10:
    print('0' + str(h) + ':', end='')
else:
    print(str(h) + ':', end='')
if m < 10:
    print('0' + str(m))
else:
    print(str(m))
