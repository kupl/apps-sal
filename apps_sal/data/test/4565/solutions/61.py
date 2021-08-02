def main():
    N = int(input())
    S = input()
    lst = [0] * N
    ans = N

    if S[0] == "E":
        lst[0] = 1
    for i in range(1, N):
        if S[i] == "E":
            lst[i] = lst[i - 1] + 1
        else:
            lst[i] = lst[i - 1]

    for i in range(N):
        if i == 0:
            left = 0
        else:
            left = i - lst[i - 1]
        right = lst[N - 1] - lst[i]

        if left + right < ans:
            ans = left + right

    print(ans)


def __starting_point():
    main()


__starting_point()
