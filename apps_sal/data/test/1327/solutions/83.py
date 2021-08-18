def d_patisserie_abc():
    N, M = [int(i) for i in input().split()]
    Cake = [[int(i) for i in input().split()] for j in range(N)]
    ppp, ppn, pnp, pnn = [], [], [], []
    for x, y, z in Cake:
        ppp.append(x + y + z)
        ppn.append(x + y - z)
        pnp.append(x - y + z)
        pnn.append(x - y - z)
    ppp.sort()
    ppn.sort()
    pnp.sort()
    pnn.sort()

    pts = map(lambda x: abs(sum(x)),
              (ppp[:M], ppn[:M], pnp[:M], pnn[:M], ppp[::-1][:M],
               ppn[::-1][:M], pnp[::-1][:M], pnn[::-1][:M])
              )
    return max(pts)


print(d_patisserie_abc())
