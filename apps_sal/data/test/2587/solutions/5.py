for t in range(int(input())):
    n = int(input())
    eights = (n + 3) // 4
    nines = n - eights
    print("9" * nines + "8" * eights)
