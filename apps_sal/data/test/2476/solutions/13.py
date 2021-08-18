def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * (N + 1)
    Cnt_A = [0] * (N + 1)
    for a in A:
        Cnt_A[a] += 1
        cnt = Cnt_A[a]
        C[cnt] += 1
    cum_C = []
    cu = 0
    for c in C:
        cu += c
        cum_C.append(cu)
    Ans = []
    for k in range(1, N + 1):
        ok, ng = 0, N // k + 1
        while ok + 1 < ng:
            n = ok + ng >> 1
            if cum_C[n] >= n * k:
                ok = n
            else:
                ng = n
        Ans.append(ok)
    print(("\n".join(map(str, Ans))))


main()
