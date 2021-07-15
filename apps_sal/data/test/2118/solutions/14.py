def unsort(d, left, right, k):
    if k[0] <= 0 or left >= right - 1:
        return
    k[0] -= 2
    mid = (left + right) // 2
    tmp = d[mid-1]
    d[mid-1] = d[mid]
    d[mid] = tmp
    unsort(d, left, mid, k)
    unsort(d, mid, right, k)


def main():
    k = [0]  # K needs to be a mutable integer
    n, k[0] = (int(i) for i in input().split())
    if k[0] % 2 == 0:
        print('-1')
        return
    d = [i for i in range(1, n+1)]
    k[0] -= 1
    unsort(d, 0, n, k)
    if k[0] == 0:
        print(*d)
    else:
        print('-1')


def __starting_point():
    main()
__starting_point()
