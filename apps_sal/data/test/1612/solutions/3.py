def contiene(l, s, n, m):
    j = 0
    for i in range(n):
        x = l[i]
        while j < m and (not l[i] == s[j]):
            j += 1
        if j == m and (not i == n):
            return False
    return True


def __starting_point():
    n = int(input())
    l = []
    m = []
    for i in range(n):
        s = [int(x) for x in input().split()]
        m.append(s[0])
        l.append(s[1:])
        l[i].sort()
    for i in range(n):
        canWin = True
        for j in range(n):
            if not j == i:
                if m[i] < m[j]:
                    continue
                if contiene(l[j], l[i], m[j], m[i]):
                    canWin = False
                    break
        if canWin:
            print('YES')
        else:
            print('NO')


__starting_point()
