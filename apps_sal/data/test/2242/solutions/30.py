def main():
    import collections

    S = input()

    mod_list = [0]

    for i in range(len(S)):
        index = len(S) - i - 1
        num = int(S[index])

        mod_list.append((mod_list[-1] + num * pow(10, i, 2019)) % 2019)

    CTR_mod_list = collections.Counter(mod_list).most_common()
    cnt = 0

    for i in range(len(CTR_mod_list)):
        n = CTR_mod_list[i][1]

        if (n == 1):
            break

        cnt += n * (n - 1) // 2

    print(cnt)


def __starting_point():
    main()


__starting_point()
