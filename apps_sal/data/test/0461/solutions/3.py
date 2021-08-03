n, a, b, c = [int(input()) for i in range(4)]
if n == 1:
    print(0)
else:
    print(min(a * (n - 1), b * (n - 1), min(a, b) + c * (n - 2)))
