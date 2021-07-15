def main():
    from collections import Counter
    n = int(input())
    cnt, res = dict(Counter(list(map(int, input().split())))), []
    x = cnt.get(0, 0)
    if x * 2 >= n:
        print(cnt[0])
        return
    cget, rpush = cnt.get, res.append
    if x:
        rpush(x)
        cnt[0] = 1

    def deeper(a, b, lvl):
        if cget(a + b, 0):
            c = a + b
            cnt[c] -= 1
            deeper(b, c, lvl + 1)
            cnt[c] += 1
        else:
            rpush(lvl)

    for x in cnt:
        cnt[x] -= 1
        for y in cnt:
            if cnt[y]:
                cnt[y] -= 1
                deeper(x, y, 2)
                cnt[y] += 1
        cnt[x] += 1
    print(max(res))


def __starting_point():
    main()

__starting_point()
