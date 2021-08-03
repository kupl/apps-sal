a = list(map(int, input().split()))
s = a[0] + a[1] + a[2]
if s >= 22:
    print('bust')
else:
    print('win')
