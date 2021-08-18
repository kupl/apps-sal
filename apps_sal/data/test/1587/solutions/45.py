import copy


def swap(data, i1, i2):
    tmp = data[i1]
    tmp2 = data[i2]
    data[i2] = tmp
    data[i1] = tmp2
    return data


def check_finish(data):
    out = True
    for i in range(len(data) - 1):
        if data[i] == 'W' and data[i + 1] == 'R':
            out = False
            return out
    return out


def __starting_point():
    n = int(input())
    c = list(input())
    if 'R' not in c:
        print((0))
    elif 'W' not in c:
        print((0))
    else:
        w_count = c.count('W')
        r_count = c.count('R')

        same_r_count = 0
        for i in range(r_count):
            if c[i] == 'R':
                same_r_count += 1

        A = r_count - same_r_count
        print(A)


__starting_point()
