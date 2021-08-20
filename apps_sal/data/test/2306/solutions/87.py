from collections import deque


def main():
    with open(0) as f:
        (N, *Temp) = map(int, f.read().split())
        (T, V) = (Temp[:N], Temp[N:])
        del Temp
    v_left = deque([0])
    v_right = deque([0])
    now = 0
    for (t, v) in zip(T, V):
        now = min(now + t, v)
        v_left.append(now)
    now = 0
    for (t, v) in zip(reversed(T), reversed(V)):
        now = min(now + t, v)
        v_right.appendleft(now)
    BC = [min(x, y) for (x, y) in zip(v_left, v_right)]
    S = [squareMeasure(vin, vout, vsup, t) for (vin, vout, vsup, t) in zip(BC[:N], BC[1:], V, T)]
    ans = sum(S) / 2
    print(ans)


def squareMeasure(vin, vout, vsup, t):
    vmax = (t + vout + vin) / 2
    if vmax > vsup:
        (a, b) = (vsup - vin, t + vout - vsup)
        S = (vin + vsup) * a + 2 * (b - a) * vsup + (vsup + vout) * (t - b)
    else:
        S = (vin + vmax) * (vmax - vin) + (vmax + vout) * (t + vin - vmax)
    return S


def __starting_point():
    main()


__starting_point()
