def abc055_d():
    n = int(input())
    s = str(input())
    ss = s[-1] + s + s[0]

    def solve(ini1, ini0):
        res = [None] * (n + 2)
        res[1] = ini1
        res[0] = ini0
        for i in range(1, n + 1):
            if ss[i] == 'o':
                if res[i] == 'S' and res[i - 1] == 'S':
                    res[i + 1] = 'S'
                if res[i] == 'S' and res[i - 1] == 'W':
                    res[i + 1] = 'W'
                if res[i] == 'W' and res[i - 1] == 'S':
                    res[i + 1] = 'W'
                if res[i] == 'W' and res[i - 1] == 'W':
                    res[i + 1] = 'S'
            else:
                if res[i] == 'S' and res[i - 1] == 'S':
                    res[i + 1] = 'W'
                if res[i] == 'S' and res[i - 1] == 'W':
                    res[i + 1] = 'S'
                if res[i] == 'W' and res[i - 1] == 'S':
                    res[i + 1] = 'S'
                if res[i] == 'W' and res[i - 1] == 'W':
                    res[i + 1] = 'W'
        return res
    ans = '-1'
    ini = [('S', 'S'), ('S', 'W'), ('W', 'S'), ('W', 'W')]
    for (ini1, ini0) in ini:
        res = solve(ini1, ini0)
        if res[0] == res[n] and res[1] == res[n + 1]:
            ans = ''.join(res[1:n + 1])
            break
    print(ans)


def __starting_point():
    abc055_d()


__starting_point()
