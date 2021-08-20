def prim_roots(number):
    if number == 2:
        return 1
    elif number == 4:
        return 2
    (z, h) = (1, 2)
    p = list()
    while h < number:
        k = pow(h, z, number)
        while k > 1:
            z += 1
            k = k * h % number
        if z == number - 1:
            p.append(h)
        z = 1
        h += 1
    return len(p)


print(prim_roots(int(input())))
