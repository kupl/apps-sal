def resolve():
    (N, H) = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        (a, b) = map(int, input().split())
        A[i] = a
        B[i] = b
    a_max = max(A)
    B = [b for b in B if a_max < b]
    B.sort(reverse=True)
    cnt = 0
    for b in B:
        if H <= 0:
            print(cnt)
            return
        H -= b
        cnt += 1
    cnt += -(-H // a_max)
    print(cnt)


def __starting_point():
    resolve()


__starting_point()
