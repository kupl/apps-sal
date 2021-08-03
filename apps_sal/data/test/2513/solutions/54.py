def solve(n, S):
    for i in range(4):
        ans = list()
        t = i
        for j, s in enumerate(S):
            f0 = t // 2
            f1 = t % 2
            f2 = f0 ^ (0 if s == 'o' else 1)
            ans.append('S' if f2 == 0 else 'W')
            t = ((f1 ^ f2) << 1) | f2

        if (i == t):
            x = ans[:-1]
            x.insert(0, ans[-1])
            return "".join(x)
    return "-1"


def __starting_point():
    print((solve(int(input()), input())))


__starting_point()
