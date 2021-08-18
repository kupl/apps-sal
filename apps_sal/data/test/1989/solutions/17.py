
BIT = [0] * (10**7)


def query_BIT(i):
    res = 0
    while i > 0:
        res += BIT[i]
        i -= i & (-i)
    return res


def add_to_BIT(n, p):
    while p <= n:
        BIT[p] += 1
        p += p & (-p)


def main():
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    pre = [0] * n
    suf = [0] * n

    d_map = {}
    for i in range(n):
        val = arr[i]
        if val not in d_map:
            d_map[val] = 1
        else:
            d_map[val] += 1
        pre[i] = d_map[val]

    d_map.clear()
    for i in range(n - 1, -1, -1):
        val = arr[i]
        if val not in d_map:
            d_map[val] = 1
        else:
            d_map[val] += 1
        suf[i] = d_map[val]

    ans = 0
    for i in range(n - 1, -1, -1):
        ans += query_BIT(pre[i] - 1)
        add_to_BIT(n, suf[i])
    print(ans)


main()
