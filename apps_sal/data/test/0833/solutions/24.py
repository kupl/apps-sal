def main():
    n, v = map(int, input().split())
    l = [0] * 3002
    for _ in range(n):
        a, b = map(int, input().split())
        l[a] += b
    a = res = 0
    for b in l:
        x = a + b
        if x < v:
            res += x
            a = 0
        else:
            res += v
            if a < v:
                a = x - v
            else:
                a = b
    print(res)


def __starting_point():
    main()
__starting_point()
