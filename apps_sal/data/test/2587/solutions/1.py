for _ in range(int(input())):
    n = int(input())
    eights = (n - 1) // 4 + 1
    nines = n - eights
    print('9' * nines + '8' * eights)
