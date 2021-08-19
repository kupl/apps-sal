import sys


def INP():
    return sys.stdin.readline().strip()


def INT():
    return int(INP())


def MAP():
    return list(map(int, INP().split()))


def ARR():
    return [int(i) for i in INP().split()]


def JOIN(arr, x=''):
    return x.join([str(i) for i in arr])


def EXIT(x='NO'):
    print(x)
    return


for _ in range(INT()):
    n = INT()
    arr = ARR()
    ans = list('ab' * (max(arr) // 2 + 1))
    print(JOIN(ans))
    for x in arr:
        ans[x] = 'b' if ans[x] == 'a' else 'a'
        print(JOIN(ans))
