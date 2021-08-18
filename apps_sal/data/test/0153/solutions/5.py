
def solve(n, k, M, t):
    '''
    >>> solve(3, 4, 11, [1, 2, 3, 4])
    6
    >>> solve(5, 5, 10, [1, 2, 4, 8, 16])
    7
    >>> solve(3, 2, 4, [1, 1])
    6
    >>> solve(5, 2, 10, [2, 3])
    6
    '''
    t.sort()
    k = len(t)

    T = sum(t)

    max_score = 0

    for fully_solved in range(min(n, M // T) + 1):
        score_1 = fully_solved * (k + 1)

        score_2 = 0
        remaining_time = M - T * fully_solved
        remaining_problems = n - fully_solved

        if remaining_problems > 0:
            level = 0
            while level < k:
                level_coeff = 1 if level + 1 < k else 2
                time_to_solve_level = t[level] * remaining_problems
                if time_to_solve_level <= remaining_time:
                    score_2 += remaining_problems * level_coeff
                    remaining_time -= time_to_solve_level
                else:
                    score_2 += (remaining_time // t[level]) * level_coeff
                    break
                level += 1
        score = score_1 + score_2
        max_score = max(score, max_score)

    return max_score


def main():
    n, k, M = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(solve(n, k, M, t))


def __starting_point():
    main()


__starting_point()
