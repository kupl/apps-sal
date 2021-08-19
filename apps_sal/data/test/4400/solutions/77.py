def main():
    S = input()
    flag = 0
    cnt = 0
    maxC = 0
    for i in range(len(S)):
        if S[i] == 'S':
            flag = 0
            continue
        elif flag == 0:
            cnt = 1
            flag = 1
        else:
            cnt += 1
        if maxC < cnt:
            maxC = cnt
    print(maxC)


def __starting_point():
    main()


__starting_point()
