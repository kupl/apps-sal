
def is_ok(arg, a, b, x):
    return True if a * arg + b * len(str(arg)) <= x else False


def meguru_bisect(ok, ng, a, b, x):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, a, b, x):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    a, b, x = list(map(int, input().split()))
    ans = meguru_bisect(0, 10**9 + 1, a, b, x)
    print(ans)


def __starting_point():
    main()


__starting_point()
