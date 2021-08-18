import sys

input = sys.stdin.readline


def main():
    N = int(input())
    F = []
    for _ in range(N):
        F.append(list(map(int, input().split())))
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))

    A = list(range(10))
    n = len(A)
    ans = -float('inf')
    for i in range(2 ** n):
        select = []
        score = 0
        for j in range(n):
            if (i >> j) & 1:
                select.append(A[j])
        if len(select) == 0:
            continue

        for j in range(N):
            cnt = 0
            for k in select:
                if F[j][k] == 1:
                    cnt += 1
            score += P[j][cnt]

        ans = max(ans, score)
    print(ans)


def __starting_point():
    main()


__starting_point()
