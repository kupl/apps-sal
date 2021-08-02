from heapq import heappop, heappush


def solve(field, s, t, k):
    INF = 10 ** 18
    ans = [[INF, INF] for _ in field]
    ans[s][0] = ans[s][1] = 0
    MOVE = [(-w2, 0), (-1, 1), (1, 1), (w2, 0)]

    q = [(0, 0, s, 0)]
    while q:
        cost, straight, v, direction = heappop(q)
        if v == t:
            return (cost - 1) // k + 1

        ceiling = ((cost - 1) // k + 1) * k + 1
        for di, ax in MOVE:
            u = v + di
            if field[u] == '@':
                continue
            if di == direction:
                nc = cost + 1
                ns = straight + 1
                if ns > k:
                    ns -= k
            else:
                nc = ceiling
                ns = 1
            if ans[u][ax] <= nc:
                continue
            ans[u][ax] = nc
            heappush(q, (nc, ns, u, di))

    return -1


h, w, k = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
h2 = h + 2
w2 = w + 2

field_tmp = [input() for _ in range(h)]
field = ['@' * w2]
for row in field_tmp:
    field.append('@')
    field.append(row)
    field.append('@')
field.append('@' * w2)
field = ''.join(field)
s = x1 * w2 + y1
t = x2 * w2 + y2
print((solve(field, s, t, k)))
