def getInput():
    line = input().split()
    return (int(line[0]), line[1])


def sLIS(n, s):
    ans = list(range(n, 0, -1))
    rev = []
    i = 0
    while i < n - 1:
        if s[i] == '<':
            j = i + 1
            while j < n - 1 and s[j] == '<':
                j += 1
            rev.append((i, j))
            i = j + 1
        else:
            i += 1
    for r in rev:
        (i, j) = r
        while i <= j:
            (ans[i], ans[j]) = (ans[j], ans[i])
            i += 1
            j -= 1
    return ans


def lLIS(n, s):
    ans = list(range(1, n + 1))
    rev = []
    i = 0
    while i < n - 1:
        if s[i] == '>':
            j = i + 1
            while j < n - 1 and s[j] == '>':
                j += 1
            rev.append((i, j))
            i = j + 1
        else:
            i += 1
    for r in rev:
        (i, j) = r
        while i <= j:
            (ans[i], ans[j]) = (ans[j], ans[i])
            i += 1
            j -= 1
    return ans


for _ in range(int(input())):
    (n, s) = getInput()
    "\n\t\tp = []\n\t\tc = +1 if s[0] == '<' else -1\n\t\tfor e in s[1:]:\n\t\t\tif c > 0 and e == '>':\n\t\t\t\tp.append(c)\n\t\t\t\tc = -1\n\t\t\telif c < 0 and e == '<':\n\t\t\t\tp.append(c)\n\t\t\t\tc = +1\n\t\t\telse:\n\t\t\t\tc += +1 if e == '<' else -1\n\t\tp.append(c)\n\t"
    print(*sLIS(n, s))
    print(*lLIS(n, s))
