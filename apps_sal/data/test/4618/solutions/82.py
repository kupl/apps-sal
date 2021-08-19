def main():
    s = input()
    N = len(s)
    K = int(input())
    X = set()
    for i in range(1, K + 1):
        for j in range(N - i + 1):
            X.add(s[j:j + i])
    print(sorted(X)[K - 1])


def __starting_point():
    main()


__starting_point()
