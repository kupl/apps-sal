for t in range(int(input())):
    n = int(input())
    d = [int(i) for i in input()]
    if n % 2 == 1:
        if 1 in [d[i] % 2 for i in range(0, n, 2)]:
            print(1)
        else:
            print(2)
    else:

        if 0 in [d[i] % 2 for i in range(1, n, 2)]:
            print(2)
        else:
            print(1)
