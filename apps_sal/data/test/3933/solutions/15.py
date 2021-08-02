def weatom(s=[]):
    n = len(s)
    if(n == 1):
        return s[0]
    elif(n == 2):
        return (s[1] + (s[1] - s[0]))
    else:
        d = s[1] - s[0]
        for i in range(2, n):
            if((s[i] - s[i - 1]) == d):
                if(i == n - 1):
                    return (s[i] + d)
            else:
                return s[n - 1]


def main():
    t = input()
    t = int(t)
    s = [int(x) for x in input().strip().split()]
    print(weatom(s))


def __starting_point():
    main()


__starting_point()
