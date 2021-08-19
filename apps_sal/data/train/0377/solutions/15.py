def nww(a, b):
    bigger = max(a, b)
    smaller = min(a, b)
    result = bigger
    i = 2
    while result % smaller != 0:
        result = bigger * i
        i += 1
    return result


class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        nw = nww(A, B)
        la = list([A * x for x in range(1, nw // A)])
        lb = list([B * x for x in range(1, nw // B)])
        cycle = sorted([0] + la + lb)
        return (N // len(cycle) * nw + cycle[N % len(cycle)]) % (10 ** 9 + 7)
