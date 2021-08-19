n = int(input())
x = int(input())
n %= 6
(a, b, c) = (x == 0, x == 1, x == 2)
for i in reversed(list(range(n))):
    if i % 2 == 0:
        (a, b) = (b, a)
    else:
        (b, c) = (c, b)
if a:
    print(0)
elif b:
    print(1)
else:
    print(2)
