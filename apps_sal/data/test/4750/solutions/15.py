for _ in range(int(input())):
    la, r1, lb, r2 = list(map(int, input().split()))
    if la != lb:
        print(la, lb)
    else:
        print(la, lb + 1)

