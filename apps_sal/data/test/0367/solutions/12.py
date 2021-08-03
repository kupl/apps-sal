from queue import Queue
import sys


def __starting_point():

    s = input()
    h = set()
    res = []
    for x in s:
        if x in h:
            h -= {x}
            res.append(x)
        else:
            h |= {x}
    odd = sorted(list(h))
    for i in range(0, (len(odd)) // 2):
        res.append(odd[i])
    if len(odd) % 2 == 1:
        mid = odd[len(odd) // 2]
    else:
        mid = ""
    res.sort()
    ans = "".join(res) + mid + "".join(res[::-1])
    print(ans)


__starting_point()
