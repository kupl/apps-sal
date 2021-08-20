x = list(map(str, input().split()))
if x[0] > x[1]:
    print('>')
elif x[0] < x[1]:
    print('<')
else:
    print('=')
