def read_string():
    return input()


def read_strings(return_type=iter, split=None, skip=0):
    return return_type(input().split(split)[skip:])


def read_lines(height, return_type=iter):
    return return_type(read_string() for i in range(height))


def read_number():
    return int(input())


def read_numbers(return_type=iter, skip=0):
    return return_type(int(i) for i in input().split()[skip:])


def read_values(*types, array=None):
    line = input().split()
    result = []
    for return_type, i in zip(types, list(range(len(types)))):
        result.append(return_type(line[i]))
    if array != None:
        array_type, array_contained = array
        result.append(array_type(array_contained(i) for i in line[len(types):]))
    return result


def read_array(item_type=int, return_type=iter, skip=0):
    return return_type(item_type(i) for i in input().split()[skip:])


def read_martix(height, **args):
    return_type = args["return_type"] if "return_type" in args else iter
    return_type_inner = args["return_type_inner"] if "return_type_inner" in args else return_type
    return_type_outer = args["return_type_outer"] if "return_type_outer" in args else return_type
    item_type = args["item_type"] if "item_type" in args else int
    return return_type_outer(read_array(item_type=item_type, return_type=return_type_inner) for i in range(height))


def read_martix_linear(width, skip=0, item_type=int, skiped=None):
    num = read_array(item_type=item_type, skip=skip)
    height = len(num) / width
    return [num[i * width: (i + 1) * width] for i in range(height)]


def gcd(x, y):
    while x != 0:
        y %= x
        if y == 0:
            return x
        x %= y
    return y


def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    n = read_number()
    r = list(range(max(1, n - 20), n + 1))
    print(max([lcm(lcm(x, y), z) for x in r for y in r for z in r]))


def __starting_point():
    main()


__starting_point()
