# from bisect import bisect_left
import sys

def solve(a, cmp):
    # if not a:
    #     return []
    # print(up)
    res = [-1 for _ in a]
    ptr = 0
    for id, e in enumerate(a):
        if ptr == 0 or cmp(a[res[ptr - 1]][0][1], e[0][0]):
            res[ptr] = id
            ptr += 1
    return [a[res[id]][1] for id in range(ptr)]


n = int(input())
a = [tuple(int(e) for e in line.split()) for line in sys.stdin]

up = [(e, id) for id, e in enumerate(a) if e[0] < e[1]]
down = [(e, id) for id, e in enumerate(a) if e[0] > e[1]]


up.sort(key=lambda e: -e[0][1])
down.sort(key=lambda e: e[0][1])

res = solve(up, lambda a, b: a > b)
res_down = solve(down, lambda a, b: a < b)

if len(res) < len(res_down):
    res = res_down

print(len(res))
print(" ".join(str(_ + 1) for _ in res))
