for _ in range(int(input())):
    n = int(input())
    o = (n - 1) // 4 + 1
    print((n - o) * '9' + o * '8')
