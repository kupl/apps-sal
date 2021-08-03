a, b, c = map(int, input().split())
M = 998244353


def calc(a, b):
    if a > b:
        a, b = b, a
    ans = 0
    t = 1
    for i in range(a + 1):
        ans = (ans + t) % M
        t = t * (a - i) * (b - i) * pow(i + 1, M - 2, M) % M
    return ans


ans = calc(a, b) * calc(b, c) * calc(a, c) % M
print(ans)
