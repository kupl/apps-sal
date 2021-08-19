lst = [0, 0, 4, 8]
mod = 10 ** 9 + 7
for i in range(4, 10 ** 6 + 1):
    lst.append(lst[-1] * 2 % mod)


def main(case):
    (n, m, x, y) = list(map(int, input().split()))
    line = str(x) + ' ' + str(y) + '\n'
    for i in range(1, m + 1):
        if i != y:
            line += str(x) + ' ' + str(i) + '\n'
    cur = -1
    for i in range(1, n + 1):
        if i != x:
            if cur == -1:
                for k in range(m, 0, -1):
                    line += str(i) + ' ' + str(k) + '\n'
                cur = 1
            else:
                for k in range(1, m + 1):
                    line += str(i) + ' ' + str(k) + '\n'
                cur = -1
    line.strip('\n')
    print(line)


def __starting_point():
    t = 1
    for i in range(t):
        main(i + 1)


__starting_point()
