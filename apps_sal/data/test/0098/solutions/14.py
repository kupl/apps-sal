(x, y) = map(int, input().split(' '))
(a2, b2) = map(int, input().split(' '))
(a3, b3) = map(int, input().split(' '))
if x >= a2 + a3 and y >= b2 and (y >= b3) or (x >= b2 + b3 and y >= a2 and (y >= a3)) or (x >= a2 + b3 and y >= a3 and (y >= b2)) or (x >= a3 + b2 and y >= a2 and (y >= b3)) or (y >= a2 + a3 and x >= b2 and (x >= b3)) or (y >= b2 + b3 and x >= a2 and (x >= a3)) or (y >= a2 + b3 and x >= a3 and (x >= b2)) or (y >= a3 + b2 and x >= a2 and (x >= b3)):
    print('YES')
else:
    print('NO')
