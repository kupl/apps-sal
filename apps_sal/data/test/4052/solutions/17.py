def go():

    n = int(input())

    s_raw = input()
    t_raw = input()

    s = []
    t = []

    for i in range(0, n):

        s.append(s_raw[i])
        t.append(t_raw[i])

        if s_raw.count(s[i]) != t_raw.count(s[i]) or s_raw.count(t[i]) != t_raw.count(t[i]):

            ##print(s_raw.count(s[i]), t_raw.count(s[i]), s_raw.count(t[i]), t_raw.count(t[i]))

            print(-1)
            return

    moves = []

    for i in range(0, n):  # indices in s

        if s[i] == t[i]: continue

        for j in range(i + 1, n):

            if t[i] == s[j]:  # s[i] == t[j]:

                for k in range(j - 1, i - 1, -1):

                    moves.append(k + 1)

                    old_s_k = s[k]
                    s[k] = s[k + 1]
                    s[k + 1] = old_s_k

                    # print(s)

                break

    print(len(moves))

    for m in moves:
        print(m, end=' ')
    print()

    return


go()
