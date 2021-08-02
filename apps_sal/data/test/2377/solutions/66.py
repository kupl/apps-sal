def resolve():
    '''
    code here
    '''
    N, H = [int(item) for item in input().split()]
    ab = [[int(item) for item in input().split()] for _ in range(N)]
    ab.sort(reverse=True, key=lambda x: x[1])
    a_max_ab = max(ab, key=lambda x: x[0])

    cnt = 0
    for a, b in ab:
        if b > a_max_ab[0]:
            H -= b
            cnt += 1

        if H <= 0:
            break

    if H > 0:
        cnt += H // a_max_ab[0]
        if H % a_max_ab[0] != 0:
            cnt += 1

    print(cnt)


def __starting_point():
    resolve()


__starting_point()
