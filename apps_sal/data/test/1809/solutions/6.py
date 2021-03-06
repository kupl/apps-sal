from collections import deque


def intput():
    return [int(x) for x in input().split(' ')]


def main(ws, ords):
    stack = []
    seen = set()
    for o in ords:
        if o not in seen:
            stack.append(o)
            seen.add(o)
        if len(stack) == len(ws):
            break
    s = 0
    for o in ords:
        idx = stack.index(o)
        w = [ws[b - 1] for b in stack[:idx]]
        s += sum(w)
        stack.insert(0, stack.pop(idx))
    print(s)


def parse():
    _ = intput()
    ws = intput()
    ords = intput()
    return (ws, ords)


main(*parse())
