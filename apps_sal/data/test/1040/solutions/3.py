from collections import deque


def remove_fox(stack):
    if len(stack) < 3:
        return
    p1, p2, p3 = stack.pop(), stack.pop(), stack.pop()
    jd = p3 + p2 + p1
    if jd != "fox":
        stack.append(p3)
        stack.append(p2)
        stack.append(p1)


def __starting_point():
    n = int(input())
    s = input()
    t = deque()
    for si in s:
        t.append(si)
        remove_fox(t)
    print((len(t)))


__starting_point()
