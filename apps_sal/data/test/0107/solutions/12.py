q = input()
if '1' in q:
    a = q.index('1')
    q = q[a:]
    if q.count('0') >= 6:
        print('yes')
    else:
        print('no')
else:
    print('no')
