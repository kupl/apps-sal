n, k = [int(s) for s in input().split()]
p = [int(s) for s in input().split()]

map = {}
res = []

for pi in p:
    if map.get(pi) is None:
        key = pi
        for j in range(pi, pi - k, -1):
            if j < 0:
                break
            if map.get(j) is None:
                key = j
            else:
                if map[j] >= pi - k + 1:
                    key = map[j]
                break
        for j in range(pi, key - 1, -1):
            if map.get(j):
                break
            map[j] = key
    res.append(map[pi])

print(*res, sep=" ")
