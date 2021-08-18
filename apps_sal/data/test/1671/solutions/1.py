
def solve():
    N = int(input())
    tasks = list(map(int, input().split()))
    avg = sum(tasks) // N
    missing = [max(avg - t, 0) for t in tasks]
    remaining = [max(t - avg - 1, 0) for t in tasks]

    print(max(sum(missing), sum(remaining)))


def __starting_point():
    solve()


__starting_point()
