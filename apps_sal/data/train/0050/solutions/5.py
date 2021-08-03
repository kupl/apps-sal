def inp(ai):
    cur = sum(ai) * 2 - n * 3
    yield cur
    for aii in ai:
        if aii == 1:
            cur += 1
        else:
            cur -= 1
        yield cur


def inp2(ii):
    ans = {}
    for i, iii in enumerate(ii):
        if iii not in ans:
            ans[iii] = i
    return ans


for _ in range(int(input())):
    n = int(input())
    a = iter(map(int, input().split()))
    a1 = [next(a) for _ in range(n)]
    a1.reverse()
    a2 = list(a)
    i1 = inp2(inp(a1))
    i2 = inp2((-i2i for i2i in inp(a2)))
    res = n * 2
    for k in list(i1.keys()):
        if k in list(i2.keys()):
            res = min(res, i1[k] + i2[k])
    print(res)
