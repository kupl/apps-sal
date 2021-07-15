def main():
    N, K = list(map(int, input().split(' ')))
    points = [list(map(int, input().split(' '))) for _ in range(N)]
    points.sort(key=lambda p: p[1])
    ans = 10**19
    for b in range(N):
        bottom = points[b][1]
        for t in range(b + K - 1, N):
            top = points[t][1]
            target_points = points[b:(t+1)].copy()
            target_points.sort(key=lambda p: p[0])
            M = len(target_points)
            for left in range(M):
                right = left + K - 1
                if right >= M:
                    break
                width = target_points[right][0] - target_points[left][0]
                ans = min([ans, width * (top - bottom)])
    print(ans)


def __starting_point():
    main()
__starting_point()
