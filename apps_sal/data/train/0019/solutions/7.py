from collections import deque

t = int(input())
for i in range(t):
    n, k, dp = [int(x) for x in input().split()]
    d = {}
    i = 0
    p = deque()
    cur = 0
    min = k
    for el in input().split():
        i += 1
        if i <= dp:
            p.append(el)
            if el in list(d.keys()):
                d[el] += 1
            else:
                d[el] = 1
                cur += 1
        else:
            if cur < min:
                min = cur
            # deleting
            exc = p.popleft()
            if d[exc] == 1:
                d.pop(exc)
                cur -= 1
            else:
                d[exc] -= 1
            # adding
            p.append(el)
            if el in list(d.keys()):
                d[el] += 1
            else:
                d[el] = 1
                cur += 1
        # print(d,p)
    if min > cur:
        min = cur
    print(min)
