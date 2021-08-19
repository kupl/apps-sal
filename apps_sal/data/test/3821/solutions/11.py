def C():
    n = int(input())
    tmp = input()
    tmp = tmp.split()
    probability = list(map(float, tmp))
    probability.sort()
    current = probability[n - 1]
    pre = 1 - probability[n - 1]
    for i in range(n - 2, -1, -1):
        tmp = current * (1 - probability[i]) + pre * probability[i]
        if tmp > current:
            current = tmp
            pre = pre * (1 - probability[i])
    print('%.12f' % current)


def __starting_point():
    C()


__starting_point()
