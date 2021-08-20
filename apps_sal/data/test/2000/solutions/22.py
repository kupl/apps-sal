n = int(input().strip())
d = {}
for i in input().strip().split():
    x = int(i)
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
ans = 0
for i in d.keys():
    for j in range(1, 31):
        x = 2 ** j - i
        if x < i:
            continue
        elif x == i:
            ans += d[i] * (d[i] - 1) // 2
        elif x > i and x in d:
            ans += d[i] * d[x]
print(ans)
