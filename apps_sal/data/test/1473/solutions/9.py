def solve(xs):
    starts = list({x[0] for x in xs}.difference({x[1] for x in xs}))
    map_next = {x[0]:x[1] for x in xs}
    ret = starts[:]
    starts = [0]+starts
    for _ in range(len(xs) - 1):
        starts[0] = map_next[starts[0]]
        ret.append(starts[0])
        starts.reverse()
    return ret

xs = [list(map(int, input().split())) for i in range(int(input()))]
print(" ".join(map(str, solve(xs))))
