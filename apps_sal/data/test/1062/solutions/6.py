def main():
    n = int(input())
    (s, t) = (str(input()), str(input()))
    p = [[0] * 26 for _ in range(26)]
    dist = 0
    for i in range(n):
        if s[i] != t[i]:
            j = ord(s[i]) - ord('a')
            k = ord(t[i]) - ord('a')
            p[j][k] = i + 1
            dist += 1
    for i in range(26):
        for j in range(26):
            if i != j and p[i][j] > 0 and (p[j][i] > 0):
                print(dist - 2)
                print(p[i][j], p[j][i])
                return
    for i in range(26):
        for j in range(26):
            if i != j and p[i][j] > 0 and (max(p[j]) > 0):
                print(dist - 1)
                for k in range(26):
                    if p[j][k] > 0:
                        print(p[i][j], p[j][k])
                        return
    print(dist)
    print(-1, -1)


def __starting_point():
    main()


__starting_point()
