a = input().split()
(x, y, z) = list(map(int, a))
(a, b, c) = list(map(int, input().split()))
rem = 0
ans = 1
if x > a:
    ans = 0
else:
    a -= x
if y > a + b:
    ans = 0
else:
    rem = a + b + c - y
if rem < z and ans != 0:
    ans = 0
if ans == 0:
    print('NO')
else:
    print('YES')
