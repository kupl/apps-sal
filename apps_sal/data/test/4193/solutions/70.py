def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())

    for _ in range(n):
        b = int(input())

        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    A[i][j] = 0

    ans = 'No'
    for i in range(3):
        if any(A[i]) == 0:
            ans = 'Yes'
    for i in range(3):
        if any([A[0][i], A[1][i], A[2][i]]) == 0:
            ans = 'Yes'
    if any([A[0][0], A[1][1], A[2][2]]) == 0:
        ans = 'Yes'
    if any([A[0][2], A[1][1], A[2][0]]) == 0:
        ans = 'Yes'

    print(ans)


def __starting_point():
    main()

__starting_point()
