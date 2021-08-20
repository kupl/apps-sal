def main():
    (N, K) = map(int, input().split())
    S = input()
    A = []
    if S[0] == '1':
        nw = 1
    else:
        nw = -1
    for i in range(1, N):
        if S[i] == '1' and nw < 0:
            A.append(nw)
            nw = 1
        elif S[i] == '0' and nw > 0:
            A.append(nw)
            nw = -1
        else:
            nw += 2 * (S[i] == '1') - 1
    A.append(nw)
    if len(A) == 1:
        print(N)
        return
    B = [0] * (len(A) + 1)
    for i in range(len(A)):
        B[i + 1] = B[i] + abs(A[i])
    if A[0] < 0:
        fm = 0
    else:
        fm = 1
    ret = 0
    for i in range(fm, len(A), 2):
        ret = max(ret, B[min(i + 2 * K, len(B) - 1)] - B[max(i - 1, 0)])
    print(ret)


def __starting_point():
    main()


__starting_point()
