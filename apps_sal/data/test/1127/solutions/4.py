for _ in range(int(input())):
    n = int(input())
    u = list(map(int, list(input())))
    if n % 2 == 0:
        for i in range(1, n, 2):
            if u[i] % 2 == 0:
                print(2)
                break
        else:
            print(1)
    else:
        for i in range(0, n, 2):
            if u[i] % 2 == 1:
                print(1)
                break
        else:
            print(2)

