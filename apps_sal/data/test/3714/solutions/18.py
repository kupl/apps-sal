from fractions import gcd
def lcm(l):
    v = 1
    for li in l:
        v = v * li // gcd(v, li)
    return v
n, c = int(input()), [0] + list(map(int, input().split()))
f, l = [False] * (n + 1), []
for i in range(1, n + 1):
    if not f[i]:
        li, x = 0, i
        while not f[x]:
            f[x] = True
            x, li = c[x], li + 1
        if x != i:
            print(-1)
            return
        l.append(li if li % 2 else li // 2)
print(lcm(l))
