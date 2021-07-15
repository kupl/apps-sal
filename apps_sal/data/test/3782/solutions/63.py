def main():
    N, K, Q, *A = map(int, open(0).read().split())

    ans = float("inf")
    for Y in set(A):
        C = []
        tmp = []
        for a in A:
            if a >= Y:
                tmp.append(a)
            else:
                if len(tmp) >= K:
                    C += sorted(tmp)[:len(tmp) - K + 1]
                tmp = []
        if len(tmp) >= K:
            C += sorted(tmp)[:len(tmp) - K + 1]

        if len(C) >= Q:
            C.sort()
            X = C[Q - 1]
            ans = min(ans, X - Y)

    print(ans)

main()
