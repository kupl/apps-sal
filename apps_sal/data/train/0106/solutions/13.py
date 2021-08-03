
L = 0
R = 1


def main():
    buf = input()
    T = int(buf)
    n = []
    lr = []
    for i in range(T):
        buf = input()
        n.append(int(buf))
        lr.append([])
        for j in range(n[i]):
            buf = input()
            buflist = buf.split()
            lr[i].append([int(buflist[0]), int(buflist[1])])
    for i in range(T):
        lr_s = list(sorted(lr[i]))
        threshold = lr_s[0][R]
        threshold_final = None
        for j in range(1, n[i]):
            if threshold < lr_s[j][L]:
                threshold_final = threshold
                break
            elif threshold < lr_s[j][R]:
                threshold = lr_s[j][R]
        if threshold_final == None:
            print(-1)  # impossible
            continue
        answer = ""
        for j in range(n[i]):
            if lr[i][j][L] <= threshold_final:
                answer += "1"
            else:
                answer += "2"
            if j < n[i] - 1:
                answer += " "
        print(answer)


def __starting_point():
    main()


__starting_point()
