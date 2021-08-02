m, n = list(map(int, input().split()))


def solve():
    painting_time = []
    finish_time = [0 for i in range(m)]

    for _ in range(m):
        painting_time.append(list(map(int, input().split())))

    for i in range(n):
        free_at = 0
        for j in range(m):
            start = max(free_at, finish_time[j])
            finish_time[j] = start + painting_time[j][i]
            free_at = finish_time[j]

    return finish_time


def __starting_point():
    print(*solve())


__starting_point()
