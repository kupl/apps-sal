'__author__' == 'deepak Singh Mehta(learning brute force)) '


def __starting_point():
    (s, x) = list(map(int, input().split(' ')))
    if (s - x) % 2 or s < x:
        print(0)
    else:
        c = bin((s - x) // 2)[2:][::-1]
        t = bin(x)[2:][::-1]
        for i in range(len(t)):
            if t[i] == '1' and i < len(c) and (c[i] == '1'):
                print(0)
                return
        print(pow(2, bin(x)[2:].count('1')) - (2 if s == x else 0))


__starting_point()
