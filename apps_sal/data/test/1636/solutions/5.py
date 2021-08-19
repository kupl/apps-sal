n = int(input())
opens = {}
sums = [n - i for i in range(n)] + [0] * (n + 1)
for i in range(n):
    t = tuple(map(int, input().split()))
    opens[t] = 1
nums = list(map(int, input().split()))
res = 1
res_nums = []
for elem in nums:
    f = 1
    x = 0
    try:
        x = sums[elem + n]
    except:
        f = 0
    y = x + elem
    try:
        u = opens[x, y]
    except KeyError:
        f = 0
    try:
        if opens[x, y - 1] == 1:
            f = 0
    except KeyError:
        pass
    try:
        if opens[x - 1, y] == 1:
            f = 0
    except KeyError:
        pass
    if f == 0:
        res = 0
        break
    sums[elem + n] += 1
    opens[x, y] = 0
    res_nums.append((x, y))
print('YES' if res else 'NO')
if res:
    for elem in res_nums:
        print(str(elem[0]) + ' ' + str(elem[1]))
