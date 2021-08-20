def main():
    (n, a, x, b, y) = map(int, input().split(' '))
    while a != x and b != y:
        a = a + 1
        b = b - 1
        if a == n + 1:
            a = 1
        if b == 0:
            b = n
        if a == b:
            print('YES')
            return
    print('NO')
    return


main()
