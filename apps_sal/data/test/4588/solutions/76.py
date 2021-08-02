a = input().split()
b = sorted(a)

if a != b:
    print('>')

elif a[0] == a[1]:
    print('=')

else:
    print('<')
