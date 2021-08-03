def main():
    n, k = map(int, input().split())
    s = input()
    s += s
    for i in range(k):
        tmp = ""
        for j in range(0, 2 * n, 2):
            if s[j] == s[j + 1]:
                tmp += s[j]
            else:
                if s[j] == "R":
                    if s[j + 1] == "S":
                        tmp += s[j]
                    else:
                        tmp += s[j + 1]
                elif s[j] == "P":
                    if s[j + 1] == "R":
                        tmp += s[j]
                    else:
                        tmp += s[j + 1]
                else:
                    if s[j + 1] == "P":
                        tmp += s[j]
                    else:
                        tmp += s[j + 1]
        s = tmp + tmp
    print(s[0])


def __starting_point():
    main()


__starting_point()
