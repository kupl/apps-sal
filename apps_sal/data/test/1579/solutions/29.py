def main():
    N = int(input())
    X, Y = {}, {}
    for _ in range(N):
        x, y = list(map(int, input().split()))
        if x not in X:
            X[x] = set()
        X[x].add(y)
        if y not in Y:
            Y[y] = set()
        Y[y].add(x)
    r = 0
    while X:
        x, ys = X.popitem()
        tx = set([x])
        ty = set(ys)
        mx, my = set(), set(ys)
        while mx or my:
            while my:
                y = my.pop()
                mx |= Y.pop(y, set())
            tx |= mx
            while mx:
                x = mx.pop()
                my |= X.pop(x, set())
            ty |= my
        r += len(tx) * len(ty)
    return r - N


print((main()))
