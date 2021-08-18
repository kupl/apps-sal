n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))

if q == 1:
    print((0))
    return()

ans = 10 ** 10
for i, y in enumerate(a):
    li = []
    l = 0
    cnd = []
    for j, x in enumerate(a + [-1]):
        if i == j:
            continue
        if x < y:
            if l - k + 1 >= 0:
                li.sort()
                cnd += li[:l - k + 1]
            li = []
            l = 0
        else:
            li.append(x)
            l += 1

    if len(cnd) >= q - 1:
        cnd.sort()
        sub = cnd[q - 2] - y
        ans = min(ans, sub)

print(ans)
