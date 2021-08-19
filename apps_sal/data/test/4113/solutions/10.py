def main():
    n = int(input())
    cakes = range(n // 4 + 1)
    donuts = range(n // 7 + 1)
    for i in cakes:
        for j in donuts:
            if 4 * i + 7 * j == n:
                print('Yes')
                return
    print('No')


main()
