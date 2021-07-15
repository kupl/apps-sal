for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    x = sum(ar)
    y = ar.count(0)
    if x + y == 0:
        print(y + 1)
    else:
        print(y)
