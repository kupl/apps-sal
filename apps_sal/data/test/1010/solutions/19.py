def solve(n, nuts):

    try:
        i = nuts.index("1")
    except:
        return 0

    ri = nuts.rindex("1")

    if i == ri:
        return 1

    res = 1
    start = i
    cur = start + 1
    while cur <= ri:
        if nuts[cur] == "1":
            res *= (cur - start)
            start = cur
            cur = start + 1
        else:
            cur += 1
    return res


def __starting_point():

    n = int(input())
    nuts = "".join(input().split())
    print(solve(n, nuts))


__starting_point()
