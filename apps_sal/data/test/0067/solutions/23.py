(x, y, z) = list(map(int, input().split()))
x += z
(A, B, C) = (False, False, False)
if x > y:
    A = True
elif x == y:
    B = True
else:
    C = True
x -= z
y += z
if x > y:
    A = True
elif x == y:
    B = True
else:
    C = True
if A and (not B) and (not C):
    print('+')
elif B and (not A) and (not C):
    print('0')
elif C and (not A) and (not B):
    print('-')
else:
    print('?')
