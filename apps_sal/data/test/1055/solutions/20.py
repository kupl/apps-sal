def is_sorted(a):
    prev = None
    for i in a:
        if prev is not None and i < prev:
            return False
        prev = i
    return True


def solve(a):
    if len(a) == 1:
        return 1
    if is_sorted(a):
        return len(a)
    return max(solve(a[:len(a) // 2]), solve(a[len(a) // 2:]))


def __starting_point():
    n = int(input())
    a = [int(p) for p in input().split()]
    print(solve(a))


__starting_point()
