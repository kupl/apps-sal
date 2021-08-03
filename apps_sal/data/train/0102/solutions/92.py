for i in range(int(input())):
    n = int(input())
    numbers = 0
    j = 0
    minn = 0
    for j in range(1, 10):
        if int(str(j) * len(str(n))) <= n:
            minn = j
    print(9 * (len(str(n)) - 1) + minn)
