txt = input()
L = len(txt)


def solve():
    for i in range(L - 1):
        if txt[i] == txt[i + 1]:
            return ' '.join([str(x) for x in [i + 1, i + 2]])
    for i in range(L - 2):
        if txt[i] == txt[i + 2]:
            return ' '.join([str(x) for x in [i + 1, i + 3]])
    return '-1 -1'


ans = solve()
print(ans)
