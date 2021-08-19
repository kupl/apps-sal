(w, n) = map(int, input().split(' '))
r = 1
if w <= 3:
    n = 0
while n:
    if not n % w in {0, 1, w - 1}:
        r = 0
    if n % w == w - 1:
        n = n // w + 1
    else:
        n = n // w
if r:
    print('YES')
else:
    print('NO')
