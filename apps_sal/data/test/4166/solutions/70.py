def main():
    N, M = map(int, input().split())
    scs = [list(map(int, input().split())) for _ in range(M)]

    scs.sort()
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10**(N - 1))
        return
    if scs[0][0] == 1:
        if scs[0][1] == 0 and N != 1:
            print(-1)
            return
    else:
        scs.append([1, 1])

    for i in reversed(range(M - 1)):
        if scs[i][0] == scs[i + 1][0]:
            if scs[i][1] != scs[i + 1][1]:
                print(-1)
                return
            else:
                scs.pop(i + 1)

    ans = 0
    for sc in scs:
        ans += sc[1] * 10**(N - sc[0])
    print(ans)


main()
