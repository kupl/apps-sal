for _ in range(int(input())):
    n, x, y = map(int, input().split())
    mi = 1000000000
    an = []
    for d in range(1, y - x + 1):
        if (y - x) % d == 0:
            for a in range(1, x + 1):
                arr = [a + d * i for i in range(n)]
                if x in arr and y in arr:
                    if mi > arr[-1]:
                        mi = arr[-1]
                        ans = arr
    print(*ans)
