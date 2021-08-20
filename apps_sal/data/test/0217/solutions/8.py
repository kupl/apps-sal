from sys import stdin, stdout
(a, b, f, k) = map(int, stdin.readline().split())
(ans, position) = (0, 0)
current = b
label = 1
for i in range(k):
    if not position:
        distance = a + a - f
        curd = a - f
        last = a
        oil = f
    else:
        distance = a + f
        curd = f
        last = 0
        oil = a - f
    if distance <= current or (a <= current and i == k - 1):
        current -= a
    elif oil <= current:
        ans += 1
        current = b - curd
    else:
        current = -1
    position = last
    if current < 0:
        label = 0
if not label:
    stdout.write('-1')
else:
    stdout.write(str(ans))
