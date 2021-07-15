def find(base, indexes):
    n = len(indexes)
    ng = -1
    ok = n

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if indexes[mid] > base:
            ok = mid
        else:
            ng = mid

    return indexes[0] if ok == n else indexes[ok]


s = input()
t = input()

s_set = set(s)
t_set = set(t)

if t_set.issubset(s_set) is False:
    print((-1))
    return

s_indxes = [[] for _ in range(26)]

for i in range(len(s)):
    c = s[i]
    idx = ord(c) - ord("a")
    s_indxes[idx].append(i)

base = -1
loop = 0
for i in range(len(t)):
    c = t[i]
    idx = ord(c) - ord("a")
    n_base = find(base, s_indxes[idx])

    if n_base <= base:
        loop += 1

    base = n_base

print((loop * len(s) + base + 1))

