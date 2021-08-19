n = int(input())


def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)


if n % digitSum(n) == 0:
    print('Yes')
else:
    print('No')
