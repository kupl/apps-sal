def solve(num):
    return num[0] == '1' and all(x == '' or x == '4' or x == '44' for x in num.split('1'))


def __starting_point():
    num = input()
    is_magical = solve(num)
    print('YES' if is_magical else 'NO')


__starting_point()
