n, m, x = list(map(int, input().split()))
ca = [list(map(int, input().split())) for _ in range(n)]


def binary(i, cost, und):
    if i == n:
        for j in range(m):
            if und[j] < x:
                return float('inf')
        return cost

    left = binary(i + 1, cost, und)
    right = binary(i + 1, cost + ca[i][0], [und[k] + ca[i][k + 1] for k in range(m)])

    mi = min(left, right)

    return mi


ans = binary(0, 0, [0] * m)
if ans == float('inf'):
    print((-1))
else:
    print(ans)
