inp = input().split(' ')


def result(sets, maximum_divisor):
    output = list()
    output.append(str(int(maximum_divisor) * (6 * int(sets) - 1)))
    for i in range(int(sets)):
        output.append(str(int(maximum_divisor) * (6 * int(i) + 1)) + ' ' + str(int(maximum_divisor) * (6 * int(i) + 3)) + ' ' + str(int(maximum_divisor) * (6 * int(i) + 4)) + ' ' + str(int(maximum_divisor) * (6 * int(i) + 5)))
    return output


for i in result(inp[0], inp[1]):
    print(i)
