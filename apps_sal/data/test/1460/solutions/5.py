def solve():
    n = int(input())
    print(3 * (n + 1) + 1)
    for i in range(n + 1):
        print(i, i)
        print(i + 1, i)
        print(i, i + 1)
    print(n + 1, n + 1)


solve()

