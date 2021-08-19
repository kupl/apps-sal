def main():
    S = input()
    K = int(input())
    ans = '1'
    tmp = -1
    for (i, s) in enumerate(S):
        if s != '1':
            ans = s
            break
        else:
            tmp = i
    if K - 1 <= tmp:
        ans = '1'
    print(ans)


def __starting_point():
    main()


__starting_point()
