from math import gcd


def canHash(n, ln):
    if n == '0' * ln:
        return ln
    ans = 0
    yes = []
    for i in range(1, ln):
        if ln % i == 0:
            token = 1
            for k in range(i):
                a = sum([int(b) for b in n[k::i]])
                if a % 2 != 0:
                    token = 0
            if token == 1:
                yes.append(i)
                ans += 1
        else:
            if gcd(ln, i) in yes:
                ans += 1
    return ans


def __starting_point():
    ln = int(input())
    print(canHash(input(), ln))


__starting_point()
