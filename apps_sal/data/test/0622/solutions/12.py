def rec(depth, pos):
    if pos > 2 ** (depth - 1):
        rec(depth - 1, pos - 2 ** (depth - 1))
    elif pos == 2 ** (depth - 1):
        print(depth)
        return
    else:
        rec(depth - 1, pos)
    return


(n, k) = [int(i) for i in input().split()]
rec(n, k)
