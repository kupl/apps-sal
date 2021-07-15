# for _ in range(1):
for _ in range(int(input())):
    x, y, n = map(int, input().split())
    # n = int(input())
    # arr = list(map(int, input().split()))
    # s = input()
    r = n % x
    if r < y:
        n -= n % x + 1
    n -= n % x - y
    print(n)
