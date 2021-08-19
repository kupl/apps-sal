"""
Codefoces #248 Div. 2
Problem A
Solver
"""
input()
l = [int(i) for i in input().split(' ')]
c = [l.count(100), l.count(200)]
if c[1] & 1:
    c[0] -= 2
    c[1] += 1
if c[0] >= 0 and (not c[0] & 1):
    print('YES')
else:
    print('NO')
