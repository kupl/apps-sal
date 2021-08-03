m, n = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]
cost = [int(x) for x in input().split()]
costa = []
i = 1
for item in cost:
    a = [item, i, r[i - 1]]
    costa.append(a)
    i += 1
counter = 0
costa.sort(reverse=True)
dic = {}
i = 0
for item in costa:
    dic[item[1]] = i
    i += 1
index = len(costa) - 1
for item in range(n):
    counter = 0
    a, b = [int(x) for x in input().split()]
    if r[a - 1] >= b:
        counter += cost[a - 1] * b
        r[a - 1] -= b
        costa[dic[a]][2] -= b
    else:
        i = index
        counter += cost[a - 1] * r[a - 1]
        costa[dic[a]][2] = 0
        b -= r[a - 1]
        r[a - 1] = 0
        while i >= 0:
            if costa[i][2] >= b:
                counter += costa[i][0] * b
                r[costa[i][1] - 1] -= b
                costa[i][2] -= b
                break
            else:
                counter += costa[i][0] * costa[i][2]
                r[costa[i][1] - 1] = 0
                index -= 1
                b -= costa[i][2]
                costa[i][2] = 0
            i -= 1
        else:
            counter = 0
    print(counter)
