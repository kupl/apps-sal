for case in range(int(input())):
    a, b = [int(x) for x in input().split()]
    a, b = [min(a,b), max(a, b)]

    x = (a+b)//3
    print(min(x, a, b))
