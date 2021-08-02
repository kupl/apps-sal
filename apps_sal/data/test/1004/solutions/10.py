n = int(input())
a = list(map(int, input().split()))


def work():
    c, d = set(), set()
    r = [0]
    for x in a:
        r[-1] += 1
        if x > 0:
            if x in c:
                return 0
            if x in d:
                return 0
            c.add(x)
            d.add(x)
        if x < 0:
            if -x not in c:
                return 0
            c.remove(-x)
            if not c:
                r.append(0)
                d = set()
    return 0 if r[-1] else r[:-1]


ans = work()
if ans:
    print(len(ans))
    print(*ans)
else:
    print(-1)
