for i in range(int(input())):
    n = int(input())
    k = int(n / 2)
    if k % 2 == 1:
        print('NO')
    else:
        print('YES')
        s1 = 0
        for i in range(k):
            print(2 * (i + 1), end=' ')
            s1 += 2 * (i + 1)
        s2 = 0
        for i in range(k - 1):
            print(2 * i + 1, end=' ')
            s2 += 2 * i + 1
        print(s1 - s2)
