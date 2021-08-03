def main():
    INF = float("inf")

    N, *S = list(map(int, open(0).read().split()))
    M = len(S)

    S.sort(reverse=True)

    Q = [S[0]]
    S[0] = INF
    for _ in range(N):
        Q.sort()
        T = Q[:]

        cur = 1
        while Q:
            p = Q.pop()
            while S[cur] >= p:
                cur += 1
                if cur == M:
                    print("No")
                    return
            T.append(S[cur])
            S[cur] = INF

        Q = T

    print("Yes")


main()
