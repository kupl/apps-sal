for i in range(int(input())):
    (a, b) = map(int, input().split())
    operations = 0
    (a, b) = (max(a, b), min(a, b))
    while b != 0:
        operations += a // b
        a -= a // b * b
        (a, b) = (max(a, b), min(a, b))
    print(operations)
