import collections


def do():
    n = int(input())
    nums = [0] + [int(c) - 1 for c in input().split(" ")]
    g = collections.defaultdict(list)
    for i, j in enumerate(nums):
        if i != j:
            g[j].append(i)
    cur = [0]
    res = 0
    while cur:
        res += len(cur) % 2
        next = []
        for c in cur:
            for nei in g[c]:
                next.append(nei)
        cur = next
    return res


print(do())
