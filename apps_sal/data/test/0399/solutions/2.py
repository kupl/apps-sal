def main():
    (y, x) = map(int, input().split())
    if x == 1 and y == 0:
        print('Yes')
        return
    if x < 1:
        print('No')
        return
    if x - y > 1:
        print('No')
        return
    if (x + y) % 2 == 0:
        print('No')
        return
    if x == 1 and y == 1:
        print('No')
    if x == 1 and y > 0:
        print('No')
        return
    print('Yes')


main()
