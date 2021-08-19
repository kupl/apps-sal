def main():
    num = 10 ** 10
    startnum = 0
    iio = '110'
    N = int(input())
    T = input()
    if T == '1':
        return print(num * 2)
    if T == '0':
        return print(num)
    if T == '11':
        return print(num)
    if T[0] == '1' and T[1] == '1' and (T[2] == '0'):
        startnum = 0
    if T[0] == '1' and T[1] == '0':
        startnum = 1
    if T[0] == '0':
        startnum = 2
    for i in range(N):
        if T[i] != iio[(i + startnum) % 3]:
            return print(0)
    if (N - (3 - startnum)) % 3 == 0:
        return print(num - (N - (3 - startnum)) // 3)
    else:
        return print(num - (N - (3 - startnum)) // 3 - 1)


def __starting_point():
    main()


__starting_point()
