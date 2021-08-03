t = int(input())
for i in range(t):
    n = int(input())
    print(2)
    print(n - 1, n)
    for i in range(n - 2, 0, -1):
        print(i, i + 2)
