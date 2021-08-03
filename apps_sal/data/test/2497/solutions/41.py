def main():
    R_edge, L_edge, U_edge, D_edge = [None] * 3, [None] * 3, [None] * 3, [None] * 3
    n = int(input())
    xyd = [input().split() for _ in [0] * n]
    xyd = [(int(x), int(y), d) for x, y, d in xyd]
    for x, y, d in xyd:
        if d in ["R", "L"]:
            if U_edge[1] is None:
                U_edge[1] = y
            else:
                U_edge[1] = max(U_edge[1], y)
            if D_edge[1] is None:
                D_edge[1] = y
            else:
                D_edge[1] = min(D_edge[1], y)
        else:
            if R_edge[1] is None:
                R_edge[1] = x
            else:
                R_edge[1] = max(R_edge[1], x)
            if L_edge[1] is None:
                L_edge[1] = x
            else:
                L_edge[1] = min(L_edge[1], x)
        for p, q, r in [[R_edge, "R", x], [L_edge, "L", x], [U_edge, "U", y], [D_edge, "D", y]]:
            if d == q:
                if p[0] is None:
                    p[0] = r
                    p[2] = r
                else:
                    p[0] = min(p[0], r)
                    p[2] = max(p[2], r)

    def area(t):
        RL, UD = [], []
        if R_edge[0] is not None:
            RL += [t + R_edge[0], t + R_edge[2]]
        if R_edge[1] is not None:
            RL += [R_edge[1]]
        if L_edge[0] is not None:
            RL += [-t + L_edge[0], -t + L_edge[2]]
        if L_edge[1] is not None:
            RL += [L_edge[1]]
        if U_edge[0] is not None:
            UD += [t + U_edge[0], t + U_edge[2]]
        if U_edge[1] is not None:
            UD += [U_edge[1]]
        if D_edge[0] is not None:
            UD += [-t + D_edge[0], -t + D_edge[2]]
        if D_edge[1] is not None:
            UD += [D_edge[1]]
        if len(RL) * len(UD) == 0:
            return 0
        else:
            return (max(RL) - min(RL)) * (max(UD) - min(UD))

    t = [0]
    for edge in [R_edge, L_edge, U_edge, D_edge]:
        if None not in edge:
            t.append(abs(edge[1] - edge[0]))
            t.append(abs(edge[1] - edge[2]))
    for edge1, edge2 in [[R_edge, L_edge], [U_edge, D_edge]]:
        if None not in [edge1[1], edge2[0]]:
            t.append(abs(edge1[1] - edge2[0]))
            t.append(abs(edge1[1] - edge2[2]))
        if None not in [edge2[1], edge1[0]]:
            t.append(abs(edge2[1] - edge1[0]))
            t.append(abs(edge2[1] - edge1[2]))
        if None not in [edge1[0], edge2[0]]:
            for i in [0, 2]:
                for j in [0, 2]:
                    t.append(abs(edge2[i] - edge1[j]) / 2)

    print((min([area(i) for i in t])))


main()
