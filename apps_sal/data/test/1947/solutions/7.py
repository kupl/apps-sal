n, q, k = list(map(int, input().split(' ')))

a = list(map(int, input().split(' ')))

count = 0


def verify(x):
    if(x < 0) or (x >= n):
        return False

    return (a[x] > k)


for i in range(n):
    if verify(i):
        count += 1

        if verify(i - 1):
            count -= 1


def cut(i):
    if not verify(i):
        return 0

    result = 1

    if verify(i - 1):
        result -= 1

    if verify(i + 1):
        result -= 1

    return result


for i in range(q):
    line = input()
    if(line == '0'):
        print(count)
    else:
        _, x, y = list(map(int, line.split(' ')))
        x -= 1

        if not verify(x):
            a[x] += y
            count += cut(x)
        else:
            a[x] += y
