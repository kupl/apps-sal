from statistics import median


def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = list(map(int, input().split()))
    ans = median(b) - median(a)
    if n % 2 == 0:
        ans *= 2
    ans = int(ans)
    ans += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
