(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
if b - c >= 0:
    print('delicious')
elif b - c >= -a:
    print('safe')
else:
    print('dangerous')
