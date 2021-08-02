n, m = map(int, input().split())
l = [int(x) for x in input().split()]
for i in range(1, n):
    l[i] = min(l[i], 2 * l[i - 1])
c = l + [l[-1] * 2 ** i for i in range(1, 32)]


def cost(x):
    ans = 0
    for i in range(32):
        if x & (1 << i):
            ans += c[i]
    return ans


ans = cost(m)
for i in range(32):
    if not (m & (1 << i)):
        tmp = m - (m % (1 << i)) + (1 << i)
        ans = min(ans, cost(tmp))

print(ans)
