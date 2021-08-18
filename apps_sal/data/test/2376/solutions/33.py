def saiki(value, HP, num):
    if num == 0:
        value += wa[0][min(HP // base, len(wa[0]) - 1)]
        ans.append(value)
    else:
        for i in range(len(wa[num])):
            if HP - (num + base) * i >= 0:
                saiki(value + wa[num][i], HP - (num + base) * i, num - 1)
            else:
                break
    return


N, W = list(map(int, input().split()))

lis = [[] for i in range(4)]

for i in range(N):
    w, v = list(map(int, input().split()))
    if i == 0:
        base = w
    lis[w - base].append(v)

lis = list([sorted(x, reverse=True) for x in lis])

wa = [[0] for i in range(4)]

for i in range(len(wa)):
    for item in lis[i]:
        wa[i].append(wa[i][-1] + item)


ans = []
saiki(0, W, 3)


print((max(ans)))
