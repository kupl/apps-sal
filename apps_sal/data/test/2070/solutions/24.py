def main():
    mode = 'filee'
    if mode == 'file':
        f = open('test.txt', 'r')

    def get():
        return [int(x) for x in (f.readline() if mode == 'file' else input()).split()]

    def gets():
        return [str(x) for x in (f.readline() if mode == 'file' else input()).split()]
    num = 100005
    w = get()
    [g] = gets()
    [dp, s, p, count] = [[0] * num, [0] * num, {}, 0]
    for i in range(len(g)):
        dp[i] = w[ord(g[i]) - 97]
    for i in range(1, len(g) + 1):
        s[i] = s[i - 1] + dp[i - 1]
    for i in range(1, len(g)):
        if s[i] not in p:
            p[s[i]] = [0] * 26
        p[s[i]][ord(g[i - 1]) - 97] += 1
        if p[s[i]][ord(g[i]) - 97] != 0:
            count += p[s[i]][ord(g[i]) - 97]
    print(count)
    if mode == 'file':
        f.close()


def __starting_point():
    main()


__starting_point()
