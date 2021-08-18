def main():
    n, m = map(int, input().split())

    a_l = [input() for i in range(n)]
    b_l = [input() for i in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            ans = 'Yes'
            for k in range(m):
                for l in range(m):
                    if a_l[i + k][j + l] != b_l[k][l]:
                        ans = 'No'
            else:
                if ans == 'Yes':
                    print(ans)
                    return
    print(ans)


def __starting_point():
    main()


__starting_point()
