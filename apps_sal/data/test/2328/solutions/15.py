def solve(points, k, res):
    if k == 0:
        res.append(points[0])
        return
    min_diff = float('inf')
    n = len(points)
    for i in range(n - k):
        p1 = points[i]
        p2 = points[i + k]
        avg = (p1 + p2) // 2
        diff = max(abs(avg - p1), abs(avg - p2))

        if diff < min_diff:
            ans = avg
            min_diff = diff

    res.append(ans)


def main():
    t = int(input())
    res = []
    for i in range(t):
        n, k = list(map(int, input().split()))
        points = list(map(int, input().split()))
        solve(points, k, res)

    for i in res:
        print(i)


main()
