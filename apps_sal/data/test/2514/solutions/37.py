def __starting_point():
    n = int(input())
    B = [0] * (10 ** 5 + 1)
    A = list(map(int, input().split()))
    for a in A:
        B[a] += 1
    sm = sum(A)
    m = int(input())
    for j in range(m):
        (b, c) = list(map(int, input().split()))
        cnt_b = B[b]
        cnt_c = B[c]
        if cnt_b == 0:
            print(sm)
        else:
            B[b] = 0
            B[c] += cnt_b
            sm = sm + c * cnt_b - b * cnt_b
            print(sm)


__starting_point()
