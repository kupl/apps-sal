A, B = (ord(x) for x in input().split())


if A < B:
    print('<')
elif A > B:
    print('>')
else:
    print('=')
