import sys


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


def solve_of_problem():
    n = int(ii())
    data = idata()
    data1 = idata()
    if n == 1:
        if data1 == data:
            print('Yes')
        else:
            print('No')
        return
    if sorted(data) != sorted(data1):
        print('No')
        return
    if n % 2 == 1:
        if data[n // 2] != data1[n // 2]:
            print('No')
            return
        data = data[:n // 2] + data[n // 2 + 1:]
        data1 = data1[:n // 2] + data1[n // 2 + 1:]
        n -= 1
    d = dict()
    for i in range(n // 2):
        d[str(data[i]) + ' ' + str(data[n - i - 1])] = 0
        d[str(data[n - 1 - i]) + ' ' + str(data[i])] = 0
        d[str(data1[i]) + ' ' + str(data1[n - i - 1])] = 0
        d[str(data1[n - 1 - i]) + ' ' + str(data1[i])] = 0
    for i in range(n // 2):
        d[str(data[i]) + ' ' + str(data[n - i - 1])] += 1
        d[str(data[n - 1 - i]) + ' ' + str(data[i])] += 1
        d[str(data1[i]) + ' ' + str(data1[n - i - 1])] -= 1
        d[str(data1[n - 1 - i]) + ' ' + str(data1[i])] -= 1
    if min(d.values()) < 0:
        print('No')
        return
    print('Yes')
    return


for ______ in range(int(ii())):
    solve_of_problem()
