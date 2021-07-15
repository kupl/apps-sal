def main():
    N = int(input())
    T = list(map(int, input().split()))
    V = list(map(int, input().split()))
    T = [t * 2 for t in T]
    V = [v * 2 for v in V]
    Tall = sum(T)
    R = [0] * (Tall + 1)
    j = N - 1
    tc, vc, vn = T[-1], V[-1], V[-1]
    R[-1] = 0
    for i in reversed(list(range(Tall))):
        tc -= 1
        if tc == 0:
            j -= 1
            tc, vn = T[j], V[j]
        R[i] = min(R[i + 1] + 1, vc, vn)
        vc = vn
    v = 0
    d = 0.0
    j = 0
    tc, vc, vn = T[j], V[j], V[j]
    T.append(0)
    V.append(0)
    for i in range(1, Tall + 1):
        tc -= 1
        if tc == 0:
            j += 1
            tc, vn = T[j], V[j]
        vnn = min(v + 1, R[i], vc, vn)
        d += (v + vnn) / 2
        vc = vn
        v = vnn
    print((d / 4))

main()

