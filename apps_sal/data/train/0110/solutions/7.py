from collections import defaultdict as dd
def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, k = rl()
    A = rl()
    peaks = []
    for i in range(1, n - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks.append(1)
        else:
            peaks.append(0)

    best = sum(peaks[:k-2])
    curr = best
    best_l = 0
    for i in range(1, n - (k - 1)):
        curr -= peaks[i - 1]
        curr += peaks[i + k - 3]
        if curr > best:
            best = curr
            best_l = i
    return best + 1, best_l + 1



t = ri()
for i in range(t):
    print(*solve())

