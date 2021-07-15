for _ in range(int(input())):
    n = int(input())
    s = input()

    a = [int(s[i]) for i in range(0, n, 2)]
    b = [int(s[i]) for i in range(1, n, 2)]

    if n % 2 == 0:
        if any(i % 2 == 0 for i in b):
            print(2)
        else:
            print(1)
    else:
        if any(i % 2 == 1 for i in a):
            print(1)
        else:
            print(2)

