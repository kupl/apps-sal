def solve():
    n = int(input())
    w = [int(st) for st in input().split(' ')]
    w.sort()
    ans = 2 ** 31
    (ansi, ansj) = (None, None)
    for i in range(0, 2 * n - 1, 2):
        for j in range(i + 1, 2 * n, 2):
            s = 0
            for k in range(0, i - 1, 2):
                s += w[k + 1] - w[k]
            for k in range(i + 1, j - 1, 2):
                s += w[k + 1] - w[k]
            for k in range(j + 1, 2 * n - 1, 2):
                s += w[k + 1] - w[k]
            if s < ans:
                ans = s
                ansi = i
                ansj = j
    return ans


print(solve())
