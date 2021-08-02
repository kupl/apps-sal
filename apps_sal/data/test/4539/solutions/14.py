N = input()


def f(x):
    result = 0
    for i in range(len(x)):
        result += int(x[i])
    return result


if int(N) % f(N) == 0:
    print('Yes')
else:
    print('No')
