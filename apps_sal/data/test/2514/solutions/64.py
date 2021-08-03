def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    q = int(input())
    bc_lst = [list(map(int, input().split())) for _ in range(q)]

    a_max = max(a_lst)
    bc_max = 0
    for i in range(q):
        b = bc_lst[i][0]
        c = bc_lst[i][1]
        bc_max = max(b, bc_max)
        bc_max = max(c, bc_max)
    maximum = max(a_max, bc_max)

    count_lst = [0] * maximum
    for i in range(n):
        a = a_lst[i]
        count_lst[a - 1] += 1
    tmp = sum(a_lst)

    for i in range(q):
        b = bc_lst[i][0]
        c = bc_lst[i][1]

        count = count_lst[b - 1]
        tmp += count * (c - b)
        count_lst[b - 1] = 0
        count_lst[c - 1] += count

        print(tmp)


def __starting_point():
    main()


__starting_point()
