
def __starting_point():
    N = int(input())
    connect = [int(x) for x in input().split(' ')]

    M = [0] * (N + 2)
    for index, i in enumerate(connect):
        M[index + 2] = i

    i = N
    ans = [i]
    while i != 1:
        ans.append(M[i])
        i = M[i]

    ans.reverse()
    ans = [str(x) for x in ans]
    print(" ".join(ans))


__starting_point()
