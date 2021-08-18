def do():
    n = int(input())
    nums = [int(c) for c in input().split(" ")]
    valid = set()
    for i in range(64):
        count = []
        for j in range(n):
            if (1 << i) & nums[j]:
                count.append(nums[j])
            if len(count) == 3:
                return 3
        if len(count) == 2:
            valid.add(count[0])
            valid.add(count[1])
    nv = len(valid)
    valid = list(valid)
    dis = [[float('inf')] * nv for _ in range(nv)]
    for i in range(nv):
        for j in range(nv):
            if i == j:
                dis[i][j] = 0
            elif valid[i] & valid[j]:
                dis[i][j] = 1
    mp = [[_ for _ in dis[i]] for i in range(len(dis))]
    res = nv + 1
    for k in range(nv):
        for i in range(nv):
            if k != i:
                for j in range(nv):
                    if k != j and i != j:
                        res = min(res, dis[i][j] + mp[j][k] + mp[k][i])
        for i in range(nv):
            if k != i:
                for j in range(nv):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    return res if res <= nv else -1


print(do())
