n = int(input())

s = str(n)
lst = []
t = set()


def xxx(string):
    if string[0] == '0':
        return
    x = int(string)

    if x in t:
        return
    t.add(x)

    k1 = 0
    k2 = 10 ** 6
    while k2 - k1 != 1:
        k = (k1 + k2) // 2
        if k ** 2 <= x:
            k1 = k
        else:
            k2 = k
    if k1 ** 2 == x:
        lst.append(len(str(x)))

    if len(string) == 1:
        return
    for x in range(len(string)):
        xxx(string[:x] + string[x + 1:])
    return


xxx(s)
if len(lst) == 0:
    print(-1)
else:
    print(len(s) - max(lst))
