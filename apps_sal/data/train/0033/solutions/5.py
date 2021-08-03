for _ in range(int(input())):
    n = int(input())
    k = n
    print(2)
    for i in range(n - 1, 0, -1):
        print(i, k)
        if (k + i) % 2 != 0:
            k = (k + i) // 2 + 1
        else:
            k = (k + i) // 2
