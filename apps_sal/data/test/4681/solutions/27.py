n = int(input())
if n == 0:
    print(2)
elif n == 1:
    print(1)
else:
    a = 2
    b = 1
    for i in range(2, n + 1):
        c = b
        b += a
        a = c
    print(b)
