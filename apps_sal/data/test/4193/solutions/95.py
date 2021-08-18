
def main():
    A = []
    num = [1 for _ in range(101)]
    C = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    ans = 'No'

    for _ in range(3):
        for i in list(map(int, input().split())):
            A.append(i)

    N = int(input())

    for _ in range(N):
        num[int(input())] -= 1

    for c in C:
        if num[A[c[0]]] == 0 and num[A[c[1]]] == 0 and num[A[c[2]]] == 0:
            ans = 'Yes'
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
