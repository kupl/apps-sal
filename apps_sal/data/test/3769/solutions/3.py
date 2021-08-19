3


def is_good(f, p, k):
    for i in range(p):
        if f[(k * i) % p] != (k * f[i]) % p:
            return False
    return True


def gen(f, p, k, i):
    if i == p:
        return is_good(f, p, k)
    else:
        ans = 0
        for j in range(p):
            f.append(j)
            ans += gen(f, p, k, i + 1)
            f.pop()
        return ans


def solve(p, k):
    num = 0
    used = set()
    for j in range(p):
        if j not in used:
            num += 1
        i = j
        while i not in used:
            used.add(i)
            i = (i * k) % p
    return pow(p, num - (k != 1), 10 ** 9 + 7)


p, k = list(map(int, input().split()))
#print(gen([], p, k, 0))
print(solve(p, k))
