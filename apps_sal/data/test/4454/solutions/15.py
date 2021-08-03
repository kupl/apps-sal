for _ in range(int(input())):
    n = int(input())
    a = sum(list(map(int, input().split())))

    print((a + n - 1) // n)
