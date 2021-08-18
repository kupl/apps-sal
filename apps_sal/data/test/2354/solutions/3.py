def solve_query(n, i, j):
    i, j = i - 1, j - 1
    half = (n ** 2) // 2 + (n & 1)
    prev_total_nums = n * i + j
    if n % 2 == 0:
        prev_small_nums = n // 2 * i + (j // 2 if i % 2 else (j + 1) // 2)
    else:
        prev_small_nums = (n // 2 + 1) * ((i + 1) // 2) + (n // 2) * (i // 2) + (j // 2 if i % 2 else (j + 1) // 2)
    if (i + j) % 2 == 0:
        return prev_small_nums + 1
    prev_big_nums = prev_total_nums - prev_small_nums
    return half + prev_big_nums + 1


def solve(n, queries):
    return [solve_query(n, x, y) for x, y in queries]


def __starting_point():
    n, q = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    for answer in solve(n, queries):
        print(answer)


__starting_point()
