def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * (N + 1)
    D = [0] * (N + 1)
    for a in A:
        C[a] += 1
        D[C[a]] += 1
    S = [0] * (N + 1)
    f = [0] * (N + 1)
    for x in range(1, N + 1):
        S[x] = S[x - 1] + D[x]
        f[x] = S[x] // x
    ans = []
    prev_ans = N
    for K in range(1, N + 1):
        a = prev_ans
        while True:
            if f[a] >= K or a == 0:
                break
            a -= 1
        ans.append(a)
        prev_ans = a
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
