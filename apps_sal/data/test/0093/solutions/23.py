c = input()
d = input()
A = c + d[::-1]
c = input()
d = input()
B = c + d[::-1]
A = A.replace('X', '')
B = B.replace('X', '')
A = A + A
if A.find(B) == -1:
    print('NO')
else:
    print('YES')
