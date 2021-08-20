a = input()
b = input()
if len(a) == len(b):
    if a == b:
        print('EQUAL')
    else:
        print('GREATER' if a > b else 'LESS')
else:
    print('GREATER' if len(a) > len(b) else 'LESS')
