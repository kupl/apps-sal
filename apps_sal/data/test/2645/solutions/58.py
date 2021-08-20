def abc046_d():
    s = str(input())
    n = len(s)
    if n == 1:
        return 0
    gc = [0] * n
    pc = [0] * n
    for (i, c) in enumerate(s):
        gc[i] = gc[i - 1] + c.count('g')
        pc[i] = pc[i - 1] + c.count('p')
    ans = (gc[-1] - pc[-1]) // 2
    return ans


def __starting_point():
    print(abc046_d())


__starting_point()
