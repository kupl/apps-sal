def __starting_point():
    s = input()
    pos = [-1]
    for i, x in enumerate(s):
        if x == '*':
            pos.append(i)

    pos.append(len(s))
    max_v = 0

    for i in range(len(pos) - 1):
        for j in range(i + 1, len(pos)):
            a = pos[i] + 1
            b = pos[j]
            ns = s[:a] + '(' + s[a : b] + ')' + s[b:]
            e = eval(ns)
            if e > max_v:
                max_v = e

    print(max_v)
__starting_point()
