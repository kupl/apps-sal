from heapq import heappop, heappush
inf = float('inf')
N = int(input())
A = list(map(int, input().split()))
sum_max = [0] * (3 * N + 1)
sum_min = [0] * (3 * N + 1)


def init_max():
    res = 0
    hq = []
    for (i, a) in enumerate(A):
        if len(hq) < N:
            heappush(hq, a)
            res += a
        elif hq[0] < a:
            res -= heappop(hq)
            heappush(hq, a)
            res += a
        sum_max[i + 1] = res


def init_min():
    res = 0
    hq = []
    for (i, a) in enumerate(A[::-1]):
        if len(hq) < N:
            heappush(hq, -a)
            res += a
        elif -hq[0] > a:
            res -= -heappop(hq)
            heappush(hq, -a)
            res += a
        sum_min[i + 1] = res


init_max()
init_min()
ans = -inf
for k in range(N, 2 * N + 1):
    res = sum_max[k] - sum_min[3 * N - k]
    ans = max(ans, res)
print(ans)
