def main():
    s = input()
    k = int(input())
    ans = 0
    tyou = 500000000000000
    for v in s:
        if v == '1':
            ans += 1
        else:
            ans += tyou ** int(v)
        if ans >= k:
            print(v)
            return


def __starting_point():
    main()
__starting_point()
