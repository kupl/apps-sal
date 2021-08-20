def ok(x):
    x = x.lower()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i.lower() not in x:
            return False
    return True


a = int(input())
b = input()
if ok(b):
    print('YES')
else:
    print('NO')
