def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    n = int(input())
    a = [0] + list(map(int, input().split()))
    for i in range(n, 0, -1):
        k = 1
        flag = 0
        while i * k <= n:
            flag ^= a[i * k]
            k += 1
        if flag != a[i]:
            a[i] ^= 1
    ans = [i for i in range(n + 1) if a[i] == 1]
    if ans == []:
        print(0)
    else:
        print(len(ans))
        print(*ans)


def __starting_point():
    main()


__starting_point()
