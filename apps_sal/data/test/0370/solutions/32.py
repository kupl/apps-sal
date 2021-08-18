def solve(v, u, k):
    sign_v = sign_u = 1
    swap = 1
    if abs(v) < abs(u):
        v, u = u, v
        swap = -1
    if v < 0:
        v = -v
        sign_v = -1
    if u < 0:
        u = -u
        sign_u = -1
    if v % k == 0:
        n = v // k
        res = []
        cum_u = 0
        for i in range(n):
            du = min(k, max(-k, u - cum_u))
            if (k + du) % 2:
                du += 1 if du < 0 else -1
            cum_u += du
            res.append([k * sign_v, du * sign_u][::swap])
        assert cum_u == u, (cum_u, u)
        return res
    elif v < k and v % 2 == 0:
        res = [[k, u - k], [v - k, k]]
        res = [[dv * sign_v, du * sign_u][::swap] for dv, du in res]
        return res
    else:
        m = v % k
        if (k + m) % 2:
            m -= 1
        res = [[m, k]] + solve(v - m, u - k, k)
        res = [[dv * sign_v, du * sign_u][::swap] for dv, du in res]
        return res


def test():
    inf = -1
    M = [[inf] * 1000 for _ in range(1000)]
    K = 9
    q = [(0, 0)]
    R = 100
    ans = 1
    M[0][0] = 0
    while q:
        q_new = []
        for x, y in q:
            for i in range(-K, K + 1, 2):
                ux = x + i
                uy = y + i
                if -R <= ux <= R:
                    if y + K <= R:
                        if M[ux][y + K] == inf:
                            M[ux][y + K] = ans
                            q_new.append((ux, y + K))
                    if y - K >= -R:
                        if M[ux][y - K] == inf:
                            M[ux][y - K] = ans
                            q_new.append((ux, y - K))
                if -R <= uy <= R:
                    if x + K <= R:
                        if M[x + K][uy] == inf:
                            M[x + K][uy] = ans
                            q_new.append((x + K, uy))
                    if x - K >= -R:
                        if M[x - K][uy] == inf:
                            M[x - K][uy] = ans
                            q_new.append((x - K, uy))
        q = q_new
        ans += 1
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            if M[x][y] != -1:
                if len(solve(x, y, K)) != M[x][y]:
                    print(f"!! x={x} y={y} len(solve(x, y, K))={len(solve(x, y, K))} M[x][y]={M[x][y]}")
    print("test finished")


def main():
    K = int(input())
    X, Y = list(map(int, input().split()))
    if K % 2 == 0 and (X + Y) % 2:
        print((-1))
        return
    V, U = X + Y, X - Y
    Ans = solve(V, U, K)
    print((len(Ans)))
    cum_x = cum_y = 0
    for v, u in Ans:
        x, y = (v + u) // 2, (v - u) // 2
        assert abs(x) + abs(y) == K
        cum_x += x
        cum_y += y
        print(f"{cum_x} {cum_y}")
    assert cum_x == X and cum_y == Y


main()
