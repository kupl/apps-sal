def main():
    n, m = map(int, input().split())
    a_b = [input().split() for i in range(n)]
    c_d = [input().split() for i in range(m)]

    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(abs(int(a_b[i][0]) - int(c_d[j][0])) + abs(int(a_b[i][1]) - int(c_d[j][1])))
        else:
            print(temp.index(min(temp)) + 1)


def __starting_point():
    main()


__starting_point()
