n, v = [int(c) for c in input().split()]
m = [[0, 0] for i in range(3003)]


for i in range(n):
    a, b = [int(c) for c in input().split()]
    m[a][1] += b
    m[a + 1][0] += b


res = 0

for i in range(1, 3002):
    if v <= m[i][0]:
        res += v
    else:
        from_future = v - m[i][0]
        got_fr = min(from_future, m[i][1])
        res += m[i][0] + got_fr
        m[i + 1][0] -= got_fr

print(res)
