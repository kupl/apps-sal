n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 10 ** 10
for y in a:
    li = []
    l = 0
    cnd = []
    l_cnd = 0
    for x in a + [-1]:
        if x < y:
            if l - k + 1 >= 0:
                li.sort()
                cnd += li[:l - k + 1]
                l_cnd += l - k + 1
            li = []
            l = 0
        else:
            li.append(x)
            l += 1

    if l_cnd >= q:
        cnd.sort()
        sub = cnd[q - 1] - y
        ans = min(ans, sub)

print(ans)
