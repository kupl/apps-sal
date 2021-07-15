#!python3

# input
A, B, C = list(map(int, input().split()))


def main():
    m = max(A, B, C)
    s = sum([m - A, m - B, m - C])
    ans = (s + 1) // 2
    if s % 2 == 1:
        ans += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
