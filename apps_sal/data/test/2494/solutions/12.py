k = int(input())

INF = 10 ** 6

d = [INF for _ in range(k)]

d[1] = 1
temp = [[1,1]]
while 1:
    next = []
    for p, c in temp:
        if c + 1 < d[(p + 1) % k]:
            d[(p + 1) % k] = c + 1
            next.append([(p + 1) % k, c + 1])
        if c < d[(p * 10) % k]:
            d[(p * 10) % k] = c
            next.append([(p * 10) % k, c])
    if len(next) == 0:
        break
    else:
        temp = [] + next

print(d[0])
