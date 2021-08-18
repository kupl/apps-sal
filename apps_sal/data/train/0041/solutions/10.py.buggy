

def openBracket(i):
    nonlocal firstOpen, ans
    ind = index[0][firstOpen]
    a = s[i: ind + 1]
    a.reverse()
    #print(i + 1, ind + 1)
    s[i: ind + 1] = a
    ans += [[i + 1, ind + 1]]
    firstOpen += 1


def closeBracket(i):
    nonlocal firstClose, ans
    ind = index[1][firstClose]
    a = s[i: ind + 1]
    a.reverse()
    #print(i + 1, ind + 1)
    ans += [[i + 1, ind + 1]]
    s[i: ind + 1] = a
    firstClose += 1


t = int(input())
for h in range(t):
    n, k = map(int, input().split())
    s = list(input())
    ans = []
    fl = 0
    index = [[], []]
    firstOpen = 0
    firstClose = 0
    for i in range(n):
        if s[i] == "(":
            index[0] += [i]
        else:
            index[1] += [i]
    for i in range(2 * k - 2):
        if fl == 0:
            if s[i] != "(":
                openBracket(i)
            else:
                firstOpen += 1
        elif fl == 1:
            if s[i] != ")":
                closeBracket(i)
            else:
                firstClose += 1
        fl = abs(fl - 1)
    fl = 0
    for i in range(2 * k - 2, n):
        if fl == 0:
            if s[i] != "(":
                openBracket(i)
            else:
                firstOpen += 1
        elif fl == 1:
            if s[i] != ")":
                closeBracket(i)
            else:
                firstClose += 1
        if i == n // 2 - k + 2 * k - 2:
            fl = 1
    print(len(ans))
    [print(*i) for i in ans]
