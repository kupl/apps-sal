def main():
    s = input()
    n = len(s)
    if n < 26:
        print(-1)
        return
    s = list(s)
    n = len(s)
    j = 0
    x = ord('A')
    a = [0] * 26
    while j + 26 <= n:
        flag = 1
        for k in range(j, j + 26):
            if s[k] != '?':
                if a[ord(s[k]) - x] == 0:
                    a[ord(s[k]) - x] = 1
                else:
                    a = [0] * 26
                    j = j + 1
                    flag = 0
                    break
        if flag == 1:
            p = 0
            for k in range(j, j + 26):
                if s[k] == "?":
                    while a[p] != 0:
                        p += 1
                    s[k] = chr(x + p)
                    p += 1
            for i in range(n):
                if s[i] == "?":
                    s[i] = 'A'
            print("".join(s))

            return

    print(-1)


def __starting_point():
    main()


__starting_point()
