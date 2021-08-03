def main(N, M, K, A, B):
    #print(f'K: {K}, A: {A}, B: {B}')

    Ai = [0]
    for i in range(N):
        Ai.append(Ai[i] + A[i])
    #print(f'Ai: {Ai}')

    Bj = [0]
    for j in range(M):
        Bj.append(Bj[j] + B[j])
    #print(f'Bj: {Bj}')

    ans = 0
    # len(A) = N+1, len(B) = M+1
    best_i = 0
    for j in range(M + 1):
        tmp = 0
        for i in range(best_i, N + 1):
            #print(f'i: {N-i}, j: {j}')
            # if Ai[N-i] + Bj[M-j] <= K:
            if Ai[N - i] + Bj[j] <= K:
                #tmp = N - i + M - j
                tmp = N - i + j
                best_i = i
                break
        #print(f'tmp: {tmp}')
        if tmp > ans:
            ans = tmp

    return ans


def __starting_point():
    N, M, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print((main(N, M, K, A, B)))


__starting_point()
