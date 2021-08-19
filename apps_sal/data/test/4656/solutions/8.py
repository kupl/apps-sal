T = int(input())


def solve():
    [N, K] = list(map(int, input().split()))
    count = {}
    S = input()
    for c in S:
        if c not in count:
            count[c] = 0
        count[c] += 1

    def necklace_size(m):
        count_ = count.copy()
        ans = [None for _ in range(m)]
        for i in range(len(ans)):
            if ans[i] != None:
                continue
            cyclic_group = set()
            j = i
            while j not in cyclic_group:
                cyclic_group.add(j)
                j += K
                j %= m
            key = None
            val = -1
            for k in count_:
                if count_[k] >= len(cyclic_group):
                    if key == None:
                        key = k
                        val = count_[k]
                    elif count_[k] < val:
                        key = k
                        val = count_[k]
            if key == None:
                return False
            for i in cyclic_group:
                ans[i] = key
                count_[key] -= 1
        return ''.join(ans)
    for i in range(len(S), -1, -1):
        foo = necklace_size(i)
        if foo:
            return len(foo)
    return -1


for _ in range(T):
    print(solve())
