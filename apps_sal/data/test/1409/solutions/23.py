
def main():
    try:
        t = input()
        s = t.split(' ')
        n = int(s[0])
        k = int(s[1])

        t = input()
        s = t.split(' ')
        ans = 0
        for i in range(n):
            if int(s[i]) + k <= 5:
                ans = ans + 1
        print(int(ans / 3))
    except EOFError:
        return


def __starting_point():
    main()


__starting_point()
