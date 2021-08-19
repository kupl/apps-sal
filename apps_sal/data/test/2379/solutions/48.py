def main():
    (N, K, C) = list(map(int, input().split(' ')))
    S = input()
    (R, L) = ([0 for _ in range(K)], [0 for _ in range(K)])
    (index, cnt) = (0, 0)
    while cnt < K and index <= N - 1:
        if S[index] == 'o':
            R[cnt] = index
            index += C + 1
            cnt += 1
        else:
            index += 1
    S = S[::-1]
    (index, cnt) = (0, 0)
    while cnt < K and index <= N - 1:
        if S[index] == 'o':
            L[K - 1 - cnt] = N - 1 - index
            index += C + 1
            cnt += 1
        else:
            index += 1
    ans = [R[k] + 1 for k in range(K) if R[k] == L[k]]
    if len(ans) == 0:
        print('')
    else:
        for a in ans:
            print(a)


def __starting_point():
    main()


__starting_point()
