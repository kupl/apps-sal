import sys
readline = sys.stdin.readline


def solve(writer):
    N, A, B, C = list(map(int, input().split()))

    variables = {
        'A': A,
        'B': B,
        'C': C
    }

    queries = (list(readline().strip()) for _ in range(N))

    next_q = next(queries)

    for i in range(N):

        let_1, let_2 = next_q
        next_q = next(queries) if i < N - 1 else ()

        if variables[let_1] == variables[let_2] == 0:
            return False

        if variables[let_1] == variables[let_2] == 1 and let_2 in next_q \
                or variables[let_1] > variables[let_2]:
            let_1, let_2 = let_2, let_1

        variables[let_1] += 1
        variables[let_2] -= 1

        writer.append(let_1)

    return True


def main():
    
    writer = list()
    ok = solve(writer)
    
    if ok:
        print('Yes')
        for w in writer:
            print(w)
    else:
        print('No')


def __starting_point():
    main()

__starting_point()
