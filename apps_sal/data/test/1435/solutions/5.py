
def count_nine(a, i):
    while i < len(a) - 1:
        if a[i] + a[i + 1] == 9:
            break
        i += 1
    else:
        return 0, 1

    n1, c1 = count_nine(a, i + 1)
    n2, c2 = count_nine(a, i + 2)
    if n1 == n2 + 1:
        return n2 + 1, c1 + c2
    else:
        return n2 + 1, c2


def count_nine2(a):
    n_list = [0] * (len(a) + 1)
    c_list = [0] * (len(a) + 1)
    c_list[-1] = c_list[-2] = 1
    for i in range(len(a) - 2, -1, -1):
        if a[i] + a[i + 1] == 9:
            n_list[i] = n_list[i + 2] + 1
            if n_list[i + 1] == n_list[i + 2] + 1:
                c_list[i] = c_list[i + 1] + c_list[i + 2]
            else:
                c_list[i] = c_list[i + 2]
        else:
            n_list[i] = n_list[i + 1]
            c_list[i] = c_list[i + 1]
    return n_list[0], c_list[0]


n, c = count_nine2([int(x) for x in input()])
print(c)
