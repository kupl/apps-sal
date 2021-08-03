import heapq


def main():
    N = int(input())
    a = list(map(int, input().split()))

    left = [0] * (3 * N)
    right = [0] * (3 * N)

    tmp = 0
    q = []
    for i in range(N):
        heapq.heappush(q, a[i])
        tmp += a[i]
    left[N - 1] = tmp
    for i in range(N, 2 * N):
        heapq.heappush(q, a[i])
        left[i] = left[i - 1] + a[i] - heapq.heappop(q)

    tmp = 0
    q = []
    for i in range(N * 3 - 1, N * 2 - 1, -1):
        heapq.heappush(q, -a[i])
        tmp += a[i]
    right[2 * N] = tmp
    for i in range(2 * N - 1, N - 1, -1):
        heapq.heappush(q, -a[i])
        right[i] = right[i + 1] + a[i] + heapq.heappop(q)

    ans = left[N - 1] - right[N]
    for i in range(N, 2 * N):
        ans = max(ans, left[i] - right[i + 1])
    print(ans)


def __starting_point():
    main()


__starting_point()
