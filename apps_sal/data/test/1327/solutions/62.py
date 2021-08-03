import itertools
n, m = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(n)]

nums = [0, 1]
ll = list(itertools.product(nums, repeat=3))

res = 0
for i in ll:
    temp = []
    for j in range(n):
        if i[0] == 0:
            x = ab[j][0]
        else:
            x = -ab[j][0]
        if i[1] == 0:
            y = ab[j][1]
        else:
            y = -ab[j][1]
        if i[2] == 0:
            z = ab[j][2]
        else:
            z = -ab[j][2]
        temp.append(x + y + z)
    tempp = list(sorted(temp, reverse=True))
    res = max(res, sum(tempp[:m]))

print(res)
