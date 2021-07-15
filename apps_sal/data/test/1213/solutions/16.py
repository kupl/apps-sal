n, k = list(map(int, input().split()))
s = input()

if k <= n / 2:
    for i in range(k, 1, -1):
        print("PRINT", s[i - 1])
        print("LEFT")
    print("PRINT", s[0])
    for i in range(k - 1):
        print("RIGHT")
    for i in range(k, n):
        print("RIGHT")
        print("PRINT", s[i])
else:
    for i in range(k, n):
        print("PRINT", s[i - 1])
        print("RIGHT")
    print("PRINT", s[-1])
    for i in range(n - k):
        print("LEFT")
    for i in range(k - 1, 0, -1):
        print("LEFT")
        print("PRINT", s[i - 1])

