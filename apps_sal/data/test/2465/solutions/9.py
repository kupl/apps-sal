for _ in range(int(input())):
    a, b = 180, int(input())
    b = a - b
    if (a - b) % b == b % b:
        a *= 2
    ibo = a
    while b:
        a, b = b, a % b
    print(ibo // a)
