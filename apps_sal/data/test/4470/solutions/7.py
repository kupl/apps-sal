def f(n):
    s = 0
    while n % 2 == 0:
        n //= 2
        s += 1
    while n % 3 == 0:
        n //= 3
        s += 2
    while n % 5 == 0:
        n //= 5
        s += 3
    if n != 1:
        return -1
    else:
        return s


for k in range(int(input())):
    print(f(int(input())))
