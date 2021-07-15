import functools

def intput():
    return [int(x) for x in input().split(" ")]

def parse():
    _ = input()
    first = intput()
    second = intput()
    third = intput()

    return first, second, third

def main(f, s, t):
    def xor_fold(ls):
        return functools.reduce(lambda x, y: x ^ y, ls)

    f_sum = xor_fold(f)
    s_sum = xor_fold(s)
    t_sum = xor_fold(t)

    print(f_sum ^ s_sum)
    print(s_sum ^ t_sum)


main(*parse())

