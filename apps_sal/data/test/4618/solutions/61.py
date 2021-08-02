def main():
    S = input()
    N = len(S)
    K = int(input())
    top_k = []
    for i in range(N):
        for j in range(i + 1, min([i + K, N]) + 1):
            st = S[i:j]
            top_k.append(st)
            if len(top_k) > K:
                top_k = list(set(top_k))
                top_k.sort()
                top_k = top_k[:K]
    top_k.sort()
    print(top_k[-1])


def __starting_point():
    main()


__starting_point()
