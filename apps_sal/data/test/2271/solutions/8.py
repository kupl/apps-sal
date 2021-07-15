def main():
    n = int(input())
    l = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        l[a] += 1
        l[b] += 1
    res = 0
    for x in l:
        res += x * (x - 1)
    print(res // 2)


def __starting_point():
    main()

__starting_point()
