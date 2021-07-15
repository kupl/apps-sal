def main():
    N = 50
    K = int(input())
    ans = [(K // N) + i for i in range(N)]
    for i in range(K % N):
        for j in range(N):
            ans[j] += N if i == j else -1
    print(N)
    print((' '.join(map(str, ans))))


def __starting_point():
    main()

__starting_point()
