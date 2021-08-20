def main():
    S = input()
    k = int(input())
    setS = set(list(S))
    count = 0
    ans = []
    for j in range(1, k + 1):
        for i in range(len(S) - j + 1):
            ans.append(S[i:i + j])
    ans = sorted(list(set(ans)))
    print(ans[k - 1])


def __starting_point():
    main()


__starting_point()
