def main():
    n = int(input())
    s_lst = [str(input()) for _ in range(n)]
    alp = list('abcdefghijklmnopqrstuvwxyz')

    lst = []
    for i in range(n):
        count_lst = [0] * 26
        s = s_lst[i]
        for j in range(len(s)):
            s_alp = s[j]
            count_lst[alp.index(s_alp)] += 1

        lst.append(count_lst)

    minimum_lst = [0] * 26
    for i in range(26):
        minimum_count = lst[0][i]
        for j in range(n):
            minimum_count = min(minimum_count, lst[j][i])

        minimum_lst[i] = minimum_count

    answer = ''
    for i in range(26):
        alphabet = alp[i] * minimum_lst[i]
        answer += alphabet
    print(answer)


def __starting_point():
    main()


__starting_point()
