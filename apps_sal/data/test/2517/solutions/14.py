import sys
import itertools


def solve(N: int, M: int, R: int, r: 'List[int]', A: 'List[int]', B: 'List[int]', C: 'List[int]'):
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import floyd_warshall
    matrix = [[0] * N for _ in range(N)]
    for i in range(M):
        matrix[A[i] - 1][B[i] - 1] = C[i]
        matrix[B[i] - 1][A[i] - 1] = C[i]
    dist_matrix = floyd_warshall(csgraph=matrix, directed=False)
    perm = list(itertools.permutations(r))
    answer = float('inf')
    for p in perm:
        a = 0
        for index in range(len(p) - 1):
            a += dist_matrix[p[index] - 1][p[index + 1] - 1]
        answer = min(answer, a)
    print(int(answer))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    R = int(next(tokens))
    r = [int(next(tokens)) for _ in range(R)]
    A = [int()] * M
    B = [int()] * M
    C = [int()] * M
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)


def __starting_point():
    main()


__starting_point()
