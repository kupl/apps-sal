3


def main():
    s = list(map(int, input()))
    ans = [[1]]
    while ans[-1] != [0 for i in range(len(s))]:
        ans.append([0 for i in range(len(s))])
        for i in range(len(s)):
            if s[i] > 0:
                ans[-1][i] = 1
                s[i] -= 1
    print(len(ans) - 2)
    for i in range(1, len(ans) - 1):
        print(int(''.join(map(str, ans[i]))), end=' ')
    print()


main()
