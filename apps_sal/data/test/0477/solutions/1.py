3


def readln():
    return list(map(int, input().split()))


(n, m, i, j, a, b) = readln()


def solve(w, h):
    if w == 0 and h == 0:
        return 0
    if w == 0 and a < n and (h % 2 == 0):
        return h
    if h == 0 and b < m and (w % 2 == 0):
        return w
    if w == 0 or h == 0:
        return 1 << 30
    if (w + h) % 2 == 0:
        return max(w, h)
    return 1 << 30


ans = min([1 << 30] + [solve(abs(i - p) // a, abs(j - q) // b) for (p, q) in ((1, 1), (1, m), (n, 1), (n, m)) if abs(i - p) % a == 0 and abs(j - q) % b == 0])
print('Poor Inna and pony!' if ans == 2 ** 30 else ans)
