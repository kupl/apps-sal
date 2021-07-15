for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    a = arr.count(0)
    b = arr.count(1)

    if b > n // 2:
        print(b - b % 2)
        print(*[1 for _ in range(b - b % 2)])
    elif b == n // 2:
        print(a)
        print(*[0 for _ in range(a)])
    else:
        print(a - a % 2)
        print(*[0 for _ in range(a - a % 2)])

