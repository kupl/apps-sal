def main():
    n = int(input())
    L = sorted(map(int, input().split()))
    L.reverse()
    K = []
    i = 1
    while i < n:
        if L[i - 1] == L[i]:
            K.append(L[i])
            i += 1
        elif L[i - 1] - L[i] == 1:
            K.append(L[i])
            i += 1
        i += 1
    ans = 0
    for i in range(1, len(K), 2):
        ans += K[i - 1] * K[i]
    print(ans)


def __starting_point():
    main()


__starting_point()
