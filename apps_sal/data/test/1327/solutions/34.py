N, Eat = map(int, input().split())
cakes_ls = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    cakes_ls[i] = list(map(int, input().split()))

Patterns = 2**3
ans = 0
for i in range(Patterns):
    mult = [1] * 3
    for j in range(3):
        if (i >> j) & 1:
            mult[j] = -1

    value_ls = [0] * N
    for n in range(N):
        target = cakes_ls[n]
        value = 0
        for x in range(3):
            value += target[x] * mult[x]
        value_ls[n] = value
    value_ls.sort(reverse=True)
    # print(value_ls)
    # print(mult,sum(value_ls[:Eat]))
    ans = max(ans, sum(value_ls[:Eat]))
print(ans)
