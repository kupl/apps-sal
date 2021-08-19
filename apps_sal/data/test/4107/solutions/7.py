def main():
    while True:
        try:
            n, m = map(int, input().strip().split())
            s = str(input())
            print(getAns(n, m, s))
        except EOFError:
            break


def getAns(n, k, s):
    ans = [0] * (n + 10)

    s = '0' + s
    ans[0] = 0
    lrt = 0
    for i in range(1, n + 1, 1):
        while (lrt < i and (lrt < i - k or s[lrt] == '0')):
            lrt += 1
#        print('nb', s[lrt], i, lrt)
        ans[i] = ans[max(0, lrt - k - 1)] + lrt if s[lrt] == '1' else ans[i - 1] + i
        if s[i] == '1':
            for j in range(i - 1, -1, -1):
                if s[j] == '1':
                    break
                ans[j] = min(ans[j], ans[i])

#    print(ans)
    return ans[n]


def __starting_point():
    main()


__starting_point()
