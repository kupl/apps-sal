def solve():
    x, y, n = map(int, input().split())
    k = n % x
    if k >= y:
        print(n - k + y)
    else:
        print(n - x - k + y)


[solve() for i in range(int(input()))]
