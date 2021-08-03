import numpy as np

from bisect import bisect

DEBUG = False


def bisect_f(f, lo, hi):
    if DEBUG:
        assert f(lo) and not f(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid):
            lo = mid
        else:
            hi = mid
        if DEBUG:
            assert f(lo) and not f(hi)
    if DEBUG:
        assert hi - lo == 1
        assert f(lo) and not f(hi)
    return lo


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
neg = []
zero = []
pos = []
for x in A:
    if x < 0:
        neg.append(x)
    elif x == 0:
        zero.append(x)
    else:
        assert x > 0
        pos.append(x)

revAbsNeg = [-x for x in reversed(neg)]  # Reverse neg and keep magnitude only
posSq = [x ** 2 for x in pos]
negSq = [x ** 2 for x in revAbsNeg]

pos = np.array(pos, dtype=np.int64)
revAbsNeg = np.array(revAbsNeg, dtype=np.int64)


def countDistinctPairsLessThan(arr, prod):
    # Given a sorted array find the number of pairs that are < prod
    # O(N * log(N)) where N = len(arr)

    N = arr.shape[0]
    assert arr.shape == (N,)
    count3 = np.sum(
        np.minimum(np.arange(N), np.searchsorted(arr, (prod - 1) // arr, side="right"))
    )

    if DEBUG:
        count = 0
        for i, x in enumerate(arr):
            count += bisect(arr, (prod - 1) // x, 0, i)

        count2 = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * arr[j] < prod:
                    count2 += 1

        print((count, count2, count3))
        assert count == count2 == count3
    return count3


def countPairsLessThanOrEqual(arr1, arr2, prod):
    # Given two sorted arrays containing *positive* numbers only,
    # find the number of pairs between the two arrays that are <= prod
    # O(N * log(M)) where N = len(arr1), M = len(arr2)
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    count3 = np.sum(np.searchsorted(arr2, prod // arr1, side="right"))

    if DEBUG:
        count = 0
        for x in arr1:
            count += bisect(arr2, prod // x)
        count2 = 0
        for x in arr1:
            for y in arr2:
                if x * y <= prod:
                    count2 += 1
        assert count == count2 == count3
    return count3


def getIndex(prod):
    # Count number of pairs strictly less than prod
    count = 0
    if prod < 0:
        # All negatives except for the negatives with abs value less than or equal -prod
        count += len(pos) * len(neg)
        count -= countPairsLessThanOrEqual(pos, revAbsNeg, -prod)
    elif prod >= 0:
        # All negatives
        count += len(pos) * len(neg)
        if prod > 0:
            # All zeroes
            count += len(zero) * len(neg)
            count += (len(zero) * (len(zero) - 1)) // 2
            count += len(zero) * len(pos)
            # Positives with positives
            count += countDistinctPairsLessThan(pos, prod)
            # Negatives with negatives
            count += countDistinctPairsLessThan(revAbsNeg, prod)

    if DEBUG:
        count2 = 0
        for i in range(N):
            for j in range(i + 1, N):
                if A[i] * A[j] < prod:
                    count2 += 1
        assert count == count2
    return count


def solve(K):
    lo = -10 ** 18
    hi = 10 ** 18 + 1
    if DEBUG:
        assert getIndex(lo) <= K < getIndex(hi)
    prod = bisect_f(lambda prod: getIndex(prod) <= K, lo, hi)
    if DEBUG:
        assert getIndex(prod) <= K < getIndex(prod + 1)
    return prod


if DEBUG:
    for k in range((N * (N - 1)) // 2):
        print(("k", k, solve(k)))

print((solve(K - 1)))  # K is 1-indexed
