N, X = map(int, input().split())
burger = [(1, 0)]
prev = (1, 0)
for i in range(N):
    burger.append((2 * prev[0] + 1, 2 * prev[1] + 2))
    prev = burger[-1]

lev = N
cur = X - 1
ps = 0
for i in range(N + 1):
    if lev == 0:
        ps += 1
        break

    if cur == 0:
        break
    elif cur == sum(burger[lev - 1]) + 1:
        ps += burger[lev - 1][0] + 1
        break
    elif cur == sum(burger[lev]) - 1:
        ps += 2 * burger[lev - 1][0] + 1
        break

    if cur < sum(burger[lev]) / 2:
        cur -= 1
        lev -= 1
    else:
        ps += burger[lev - 1][0] + 1
        cur -= sum(burger[lev - 1]) + 2
        lev -= 1
print(ps)
