def main(N, M, K, A, B):
    Ai = [0]
    for i in range(N):
        Ai.append(Ai[i] + A[i])
    Bj = [0]
    for j in range(M):
        Bj.append(Bj[j] + B[j])
    ans = 0
    best_i = 0
    for j in range(M + 1):
        tmp = 0
        for i in range(best_i, N + 1):
            if Ai[N - i] + Bj[j] <= K:
                tmp = N - i + j
                best_i = i
                break
        if tmp > ans:
            ans = tmp
    return ans


def __starting_point():
    (N, M, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(main(N, M, K, A, B))


__starting_point()
