from collections import defaultdict


def rep(cand, succ):
    ret = set()
    for word in cand:
        for r in succ[word[0]]:
            ret.add(r + word[1:])

    return ret


n, q = list(map(int, input().split()))
succ = defaultdict(list)

for _ in range(q):
    a, b = input().split()
    succ[b].append(a)

cand = set("a")
for _ in range(n - 1):
    cand = rep(cand, succ)
print(len(cand))
