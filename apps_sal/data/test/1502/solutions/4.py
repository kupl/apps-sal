def int_to_bool(n):
    return [bool(n & 1 << i) for i in range(4)]


a = int(input())


def apply(expected, input):
    output = [False] * 4
    output[3] = not input[3]
    if input[3]:
        output[2] = not input[2]
    else:
        output[2] = input[2]
    if input[3] and input[2]:
        output[1] = not input[1]
    else:
        output[1] = input[1]
    if input[3] and input[2] and input[1]:
        output[0] = not input[0]
    else:
        output[0] = input[0]
    return output == expected


for i in range(16):
    if apply(int_to_bool(a), int_to_bool(i)):
        print(i)
