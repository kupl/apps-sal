(d, g) = map(int, input().split())
point = [[int(x) for x in input().split()] for i in range(d)]
ans = 100000000
for i in range(2 ** d):
    sub = 0
    count = 0
    complete = [False] * d
    for j in range(d):
        if i >> j & 1:
            complete[j] = True
            sub += 100 * (j + 1) * point[j][0] + point[j][1]
            count += point[j][0]
    for j in range(d - 1, -1, -1):
        if sub >= g:
            break
        if complete[j]:
            continue
        c = min((g - sub - 1) // (100 * (j + 1)) + 1, point[j][0])
        count += c
        sub += c * 100 * (j + 1)
        if c == point[j][0]:
            sub += point[j][1]
    if ans > count:
        ans = count
print(ans)
