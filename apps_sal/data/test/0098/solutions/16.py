(a, b) = map(int, input().split())
(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
flag = False
x = a1 + a2
bigger = max([b1, b2])
if x <= a:
    if bigger <= b:
        flag = True
if x <= b:
    if bigger <= a:
        flag = True
x = a1 + b2
bigger = max([b1, a1])
if x <= a:
    if bigger <= b:
        flag = True
if x <= b:
    if bigger <= a:
        flag = True
x = b1 + b2
bigger = max([a1, a2])
if x <= a:
    if bigger <= b:
        flag = True
if x <= b:
    if bigger <= a:
        flag = True
x = b1 + a2
bigger = max([a1, b2])
if x <= a:
    if bigger <= b:
        flag = True
if x <= b:
    if bigger <= a:
        flag = True
if flag:
    print('YES')
else:
    print('NO')
