def input_split(f): return list(map(f, input().split()))


def main():
    n, m = input_split(int)
    lst = [input()]
    sml = []
    for i in range(n - 1):
        lst.append(input())
        sml.append(False)

    ans = 0
    for i in range(m):
        flag = True
        for j in range(n - 1):
            flag = flag and ((lst[j][i] <= lst[j + 1][i]) or sml[j])
        if flag:
            for j in range(n - 1):
                if lst[j][i] < lst[j + 1][i]:
                    sml[j] = True
        else:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
