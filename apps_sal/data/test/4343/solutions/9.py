def to_cc26(s):
    result = [ord(v) - ord('a') for v in s]
    result.reverse()
    return result


def to_number(a):
    result = 0
    mult = 1
    for v in a:
        result += v * mult
        mult *= 26
    return result


def minus(b, a):
    index = 0
    result = []
    additional = 0
    while index < len(b):
        if b[index] >= a[index] + additional:
            result.append(b[index] - a[index] - additional)
            additional = 0
        else:
            result.append(b[index] + 26 - a[index] - additional)
            additional = 1
        index += 1
    return result


def plus(a, b):
    index = 0
    result = []
    additional = 0
    while index < len(a):
        if b[index] + a[index] + additional < 26:
            result.append(b[index] + a[index] + additional)
            additional = 0
        else:
            result.append(b[index] + a[index] + additional - 26)
            additional = 1
        index += 1
    return result


def to_str(a):
    a.reverse()
    return ''.join((chr(v + ord('a')) for v in a))


def divide_2(a):
    a.reverse()
    result = []
    index = 0
    value = 0
    while index < len(a):
        value = value * 26 + a[index]
        result.append(value // 2)
        value %= 2
        index += 1
    result.reverse()
    return result


def solve(s, t):
    b = to_cc26(t)
    a = to_cc26(s)
    diff_26 = minus(b, a)
    half_diff = divide_2(diff_26)
    result_26 = plus(a, half_diff)
    return to_str(result_26)


def main() -> None:
    n = int(input())
    s = input()
    t = input()
    print(solve(s, t))


def __starting_point():
    main()


__starting_point()
