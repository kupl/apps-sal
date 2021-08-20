n = int(input())
x = min([int(input()) for _ in range(5)])
(a, b) = divmod(n, x)
if b == 0:
    print(5 + (a - 1))
else:
    print(5 + a)
