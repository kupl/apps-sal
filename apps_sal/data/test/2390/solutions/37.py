def main():
    from sys import stdin

    def input():
        return stdin.readline().strip()

    n, c = list(map(int, input().split()))
    x, v = [0] * (n + 2), [0] * (n + 2)
    for i in range(n):
        j, k = list(map(int, input().split()))
        x[i + 1] = j
        v[i + 1] = v[i] + k
    x[n + 1] = c
    v[n + 1] = v[n]

    max_nut_clockwise = [0] * (n + 1)
    for i in range(1, n + 1):
        max_nut_clockwise[i] = max(max_nut_clockwise[i - 1], v[i] - x[i])
    max_nut_counterclockwise = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        max_nut_counterclockwise[i] = max(max_nut_counterclockwise[i + 1], v[-1] - v[i] - c + x[i + 1])

    ans = 0
    for i in range(n):
        if ans < v[i] - 2 * x[i] + max_nut_counterclockwise[i]:
            ans = v[i] - 2 * x[i] + max_nut_counterclockwise[i]
    for i in range(2, n + 2):
        if ans < v[-1] - v[i - 1] - 2 * (c - x[i]) + max_nut_clockwise[i - 1]:
            ans = v[-1] - v[i - 1] - 2 * (c - x[i]) + max_nut_clockwise[i - 1]

    print(ans)


main()
