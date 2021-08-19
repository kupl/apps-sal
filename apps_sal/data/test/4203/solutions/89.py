from re import match
if match('^A[a-z]+C[a-z]+$', input()):
    print('AC')
else:
    print('WA')
