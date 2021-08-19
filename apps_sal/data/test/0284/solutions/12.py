n = int(input())
(x, y, z) = (1234567, 123456, 1234)
a_max = n // x
b_max = n // y


def do_it():
    for a in range(a_max + 1):
        for b in range(b_max + 1):
            if a * x + b * y > n:
                break
            if (n - (a * x + b * y)) % z == 0:
                print('YES')
                return
    print('NO')


do_it()
