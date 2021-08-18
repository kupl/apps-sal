import sys
fin = sys.stdin.readline

N = int(fin())
coords = [[int(elem) for elem in fin().split(' ')] for _ in range(N)]
odd_or_even = abs((coords[0][0] + coords[0][1]) % 2)
max_sum = 0
for coord in coords:
    x, y = coord
    if (x + y) % 2 != odd_or_even:
        print((-1))
        return
    else:
        max_sum = max(max_sum, abs(x) + abs(y))

# partial solution (because m must not exceed 40)


def partial_solution(max_sum, coords):
    m = max_sum
    print(m)
    print((' '.join(['1'] * m)))
    for coord in coords:
        x, y = coord
        count = 0
        output = ""
        if x > 0:
            output += "R" * x
        else:
            output += "L" * abs(x)
        count += abs(x)

        if y > 0:
            output += "U" * y
        else:
            output += "D" * y
        count += abs(y)

        assert (m - count) % 2 == 0
        output += "LR" * ((m - count) // 2)
        print(output)
#partial_solution(max_sum, coords)


def padding(binary_expression):
    len_pad = 31 - len(binary_expression[2:])
    return "0" * len_pad + binary_expression[2:]


def full_solution(max_sum, coords, odd_or_even):
    mode_map = {(0, 0): "L",
                (1, 1): "R",
                (0, 1): "D",
                (1, 0): "U"}
    rotated_coords = [(x + y, x - y) for x, y in coords]
    d = []
    for i in range(31):
        d.append(2**i)
    if odd_or_even == 1:
        m = 31
    else:
        m = 32
        d.append(1)
    print(m)
    print((" ".join([str(d_elem) for d_elem in d])))
    if odd_or_even == 1:
        for rotated_coord in rotated_coords:
            u, v = rotated_coord
            const_2pow31 = 2**31
            flags_u = list(padding(bin((u + const_2pow31 - 1) // 2)))[::-1]
            flags_v = list(padding(bin((v + const_2pow31 - 1) // 2)))[::-1]
            flags = [(int(fu), int(fv)) for fu, fv in zip(flags_u, flags_v)]
            output = "".join([mode_map[flag] for flag in flags])
            print(output)
    else:
        for rotated_coord in rotated_coords:
            u, v = rotated_coord
            u -= 1
            v -= 1
            const_2pow31 = 2**31
            flags_u = list(padding(bin((u + const_2pow31 - 1) // 2)))[::-1]
            flags_v = list(padding(bin((v + const_2pow31 - 1) // 2)))[::-1]
            flags = [(int(fu), int(fv)) for fu, fv in zip(flags_u, flags_v)]
            output = "".join([mode_map[flag] for flag in flags]) + "R"
            print(output)


full_solution(max_sum, coords, odd_or_even)
