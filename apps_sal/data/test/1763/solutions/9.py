import sys
input = sys.stdin.readline


def bin(l, r, c):
    if l == r:
        return l
    m = (l + r + 1) // 2
    if h[m] <= c:
        return bin(m, r, c)
    else:
        return bin(l, m - 1, c)


def cost(c, move):
    res = 0
    i = 0
    if c >= h[-1]:
        i = n - 1
    else:
        i = bin(0, n - 1, c)
    res += a * ((i + 1) * c - H[i + 1])
    res += r * (H[-1] - H[i + 1] - (n - i - 1) * c)
    if move:
        res -= (a + r - m) * min((i + 1) * c - H[i + 1], H[-1] - H[i + 1] - (n - i - 1) * c)
    return res


(n, a, r, m) = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort()
H = [None] * (n + 1)
H[0] = 0
for i in range(1, n + 1):
    H[i] = H[i - 1] + h[i - 1]
move = m < a + r
if not move:
    print(min((cost(h[i], move) for i in range(n))))
else:
    tt = min(cost(H[-1] // n, move), cost(H[-1] // n + 1, move))
    ttt = min((cost(h[i], move) for i in range(n)))
    print(min(tt, ttt))
