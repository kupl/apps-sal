3

def solve(N, A):
    ans = []
    for a in range(N):
        visited = bytearray(N)
        p = a
        while True:
            if visited[p] == 1:
                ans.append(p + 1)
                break
            visited[p] = 1
            p = A[p] - 1

    return ans


def main():
    N = int(input())
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(*solve(N, A))


def __starting_point():
    main()

__starting_point()
