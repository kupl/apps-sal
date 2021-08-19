K = int(input())
P = [n for n in range(1, 10)]
Q = [n for n in range(1, 10)]
for d in range(20):
    if d < 12:
        for m in range(10, 100):
            P.append(int(str(m) + '9' * d))
            Q.append(m // 10 + m % 10 + 9 * d)
    else:
        for m in range(100, 1000):
            P.append(int(str(m) + '9' * (d - 1)))
            Q.append(sum([int(s) for s in str(m)]) + 9 * (d - 1))
L = len(P)
c = 0
for (i, (p, q)) in enumerate(zip(P, Q)):
    ok = True
    for j in range(i + 1, L):
        (np, nq) = (P[j], Q[j])
        if np * q < nq * p:
            ok = False
            break
    if ok:
        print(p)
        c += 1
    if c == K:
        break
'\nimport matplotlib.pyplot as plt\n\nA = []\nB = []\nfor n in range(-1+10**10, 10**14, 10**10):\n    m = sum([int(s) for s in str(n)])\n    A.append(n)\n    B.append(n/m)\n\n\nplt.plot(A, B)\nplt.show()\n'
