def solve():
    (n, m) = list(map(int, input().split()))
    a = [[] for _ in range(1 << 3)]
    ans = -10 ** 14
    for _ in range(n):
        s = list(map(int, input().split()))
        for i in range(1 << 3):
            tmp = 0
            for j in range(3):
                if i >> j & 1:
                    tmp += s[j]
                else:
                    tmp -= s[j]
            a[i].append(tmp)
    for x in range(1 << 3):
        res = sorted(a[x], reverse=True)
        ans = max(ans, sum(res[:m]))
    print(ans)


solve()
