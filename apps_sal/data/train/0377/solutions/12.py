def LCM(x, y):
    if x == y:
        return x
    bigger = max([x, y])
    smaller = min([x, y])
    res = bigger
    while res % smaller != 0:
        res += bigger
    return res


class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        lcm = LCM(A, B)
        div = [0, lcm]
        for i in [A, B]:
            t = i
            while t < lcm:
                div.append(t)
                t += i

        div = sorted(div)
        cycle = len(div) - 1

        return (div[N % cycle] + lcm * (N // cycle)) % 1000000007
