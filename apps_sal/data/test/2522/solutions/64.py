def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = b[::-1]

    l = []
    num = -1
    for i in range(n):
        if a[i] == b[i]:
            l.append(i)
            num = a[i]

    ind = 0
    for i in range(n):
        if b[i] != num and a[i] != num and ind < len(l):
            b[i], b[l[ind]] = b[l[ind]], b[i]
            ind += 1

    if ind < len(l):
        print('No')
    else:
        print('Yes')
        print(*b)


def __starting_point():
    solve()


__starting_point()
