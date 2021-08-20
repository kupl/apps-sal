(a, b, c) = [int(x) for x in input().split()]


def solve(a, b, c):
    for i in range(a + 1):
        l1 = i
        l2 = b - i
        l3 = a - i + l2
        if l3 == c and l3 >= 0 and (l2 >= 0) and (l2 != 0 or l3 != 0):
            print(l1, end=' ')
            print(l2, end=' ')
            print(a - i)
            return
    print('Impossible')


solve(a, b, c)
