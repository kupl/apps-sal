import numbers
(r1, i1) = map(float, input().split())
(r2, i2) = map(float, input().split())
c1 = complex(r1, i1)
c2 = complex(r2, i2)


def printer(c):
    real = c.real
    imag = c.imag
    sign = '+' if imag >= 0 else '-'
    print('{:.2f}{}{:.2f}i'.format(real, sign, abs(imag)))


def mod(c):
    return (c.real * c.real + c.imag * c.imag) ** 0.5


printer(c1 + c2)
printer(c1 - c2)
printer(c1 * c2)
printer(c1 / c2)
print('{:.2f}+0.00i'.format(mod(c1)))
print('{:.2f}+0.00i'.format(mod(c2)))
