from sys import stdin, stdout


def arrinp():
    return [*list(map(int, stdin.readline().split(' ')))]


def mulinp():
    return list(map(int, stdin.readline().split(' ')))


def intinp():
    return int(stdin.readline())


def inp():
    return stdin.readline()


def solution():
    (l, r) = mulinp()
    if r < 2 * l:
        print(-1, -1)
        return
    else:
        print(l, 2 * l)
        return


testcases = 1
testcases = intinp()
for _ in range(testcases):
    solution()
