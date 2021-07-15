def is_sorted(a, l, r):
    for i in range(l + 1, r):
        if a[i] < a[i - 1]:
            return False
    return True


def solve(a, l, r):
    if is_sorted(a, l, r):
        return r - l
    return max(solve(a, l, (r + l) // 2), solve(a, (r + l)//2, r))


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a, 0, n))


def __starting_point():
    main()

__starting_point()
