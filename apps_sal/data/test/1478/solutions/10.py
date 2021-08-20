def __starting_point():
    comments = input().split(',')
    n = len(comments) // 2
    stack = [0]
    lvl = 1
    res = []
    for i in range(n):
        (comm, child) = (comments[2 * i], int(comments[2 * i + 1]))
        while lvl > 1 and stack[lvl - 1] == 0:
            lvl -= 1
        stack[lvl - 1] -= 1
        if len(res) == lvl - 1:
            res.append([comm])
        else:
            res[lvl - 1].append(comm)
        if child > 0:
            if lvl == len(stack):
                stack.append(child)
            else:
                stack[lvl] = child
            lvl += 1
    print(len(res))
    for l in res:
        print(' '.join(l))


__starting_point()
