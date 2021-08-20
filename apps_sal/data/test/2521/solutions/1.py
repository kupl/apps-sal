from heapq import heappop, heappush, heapify


def main():
    n = int(input())
    A = list(map(int, input().split()))
    left_sums = []
    left = A[:n]
    left_sum = sum(left)
    left_sums.append(left_sum)
    heapify(left)
    for a in A[n:2 * n]:
        left_sum += a
        heappush(left, a)
        left_sum -= heappop(left)
        left_sums.append(left_sum)
    right_sums = []
    right = []
    for a in A[2 * n:]:
        right.append(-a)
    right_sum = sum(right)
    right_sums.append(-right_sum)
    heapify(right)
    for a in A[2 * n - 1:n - 1:-1]:
        right_sum += -a
        heappush(right, -a)
        right_sum -= heappop(right)
        right_sums.append(-right_sum)
    candidates = []
    for (sum1, sum2) in zip(left_sums, right_sums[::-1]):
        candidates.append(sum1 - sum2)
    print(max(candidates))


def __starting_point():
    main()


__starting_point()
