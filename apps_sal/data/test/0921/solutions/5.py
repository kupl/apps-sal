n, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a_index = [(x, i) for i, x in enumerate(a)]
a_index.sort(reverse=True)
res = [0] * len(a)
for x, i in a_index:
    need = (x + 1) // 2
    res[i] = need
    w -= need
    if w < 0:
        print(-1)
        return
if w > 0:
    for x, i in a_index:
        if w == 0:
            break
        need = min(w, x - res[i])
        res[i] += need
        w -= need
print(res[0], end="")
for i in range(1, len(res)):
    print(" " + str(res[i]), end="")
print()
