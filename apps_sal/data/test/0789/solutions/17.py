number = str(input())
ret = 0


def dothat(number, poww):
    yep = number
    for i in range(poww - 1):
        number *= yep
    if poww == 0:
        number = 1
    return number


for i in range(len(number)):
    if number[i] == '4':
        ret += dothat(2, len(number) - i - 1)
    else:
        ret += dothat(2, len(number) - i)


print(ret)
