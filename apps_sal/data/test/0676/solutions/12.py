n = int(input())
t = sorted([int(input()) for i in range(n)])
s = None
if n == 0:
    s = [1, 1, 3, 3]
elif n == 1:
    a = t[0]
    s = [a, 3 * a, 3 * a]
elif n == 2:
    (a, b) = t
    if a * 3 >= b:
        s = [3 * a, 4 * a - b]
elif n == 3:
    (a, b, c) = t
    if 4 * a == b + c:
        s = [3 * a]
    elif 4 * c / 3 == a + b:
        s = [c // 3]
    elif c == 3 * a:
        s = [4 * a - b]
elif n == 4:
    (a, b, c, d) = t
    if d + a == 4 * a == b + c:
        s = []
if s != None:
    print('YES')
    for a in s:
        print(a)
else:
    print('NO')
