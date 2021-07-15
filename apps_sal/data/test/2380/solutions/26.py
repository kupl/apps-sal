def main():
    N, M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    A.sort()


    bc = [[int(i) for i in input().split()] for _ in range(M)]
    bc.sort(key=lambda x: x[1])


    ai = N - 1
    mi = M - 1
    pos = 0
    ans = 0
    for _ in range(N):
        if (A[ai] > bc[mi][1]) | (mi < 0):
            pos += 1
            ans += A[ai]
            ai -= 1
        elif pos + bc[mi][0] >= N:
            ans += bc[mi][1] * (N - pos)
            break
        else:
            ans += bc[mi][0] * bc[mi][1]
            pos += bc[mi][0]
            mi -= 1
        if pos >= N:
            break

    print(ans)



def __starting_point():
    main()

__starting_point()
