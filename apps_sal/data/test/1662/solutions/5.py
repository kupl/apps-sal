__author__ = 'Adela'


def main():
    m = int(input())
    b = [0 for i in range(0, 5001)]
    res = []
    maxi = 0
    for k in input().split():
        nr = int(k)
        b[nr] += 1
        if nr > maxi:
            maxi = nr
    for i in range(0, maxi + 1):
        if b[i] != 0:
            res.append(i)
            b[i] -= 1
    for j in range(maxi - 1, 0, -1):
        if b[j] != 0:
            res.append(j)
    print(len(res))
    for k in res:
        print(k, end=' ')


def __starting_point():
    main()


__starting_point()
