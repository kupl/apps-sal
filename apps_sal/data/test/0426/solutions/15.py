def main():
    n, k = map(int, input().split())
    S = input().strip()
    if n == 1:
        if k == 0:
            return S
        return 0
    cnt = 0
    ret = ''
    for i, s in enumerate(S):
        if cnt == k:
            ret += s
        elif i == 0:
            ret += '1'
            if s != '1':
                cnt += 1
        else:
            ret += '0'
            if s != '0':
                cnt += 1
    return ret


def __starting_point():
    print(main())


__starting_point()
