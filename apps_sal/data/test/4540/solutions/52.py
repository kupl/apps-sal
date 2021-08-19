def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    a_lst.insert(0, 0)
    a_lst.append(0)
    lst = []
    for i in range(n + 1):
        lst.append(abs(a_lst[i + 1] - a_lst[i]))
    tmp = sum(lst)
    tmp1 = sum(lst)
    answer_lst = []
    for i in range(n):
        for j in range(2):
            tmp1 -= lst[i + j]
        tmp1 += abs(a_lst[i + 2] - a_lst[i])
        answer_lst.append(tmp1)
        tmp1 = tmp
    for i in range(n):
        print(answer_lst[i])


def __starting_point():
    main()


__starting_point()
