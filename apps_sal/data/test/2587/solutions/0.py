for _ in range(int(input())):
    n = int(input())
    x = (n + 3) // 4
    y = n - x
    print(y * '9' + x * '8')
