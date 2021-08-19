def __starting_point():
    n = int(input())
    s = str(input())
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            print('YES')
            print(i + 1, i + 2)
            quit()
    print('NO')


__starting_point()
