from collections import defaultdict


def solve():
    n = int(input())
    A = [int(k) for k in input().split()]

    mod = 998244353

    freq = defaultdict(list)

    for i in range(n):
        freq[A[i]].append(i)

    C = []
    i = 0
    cache = set()

    while i < n:
        C.append(0)
        cache.add(A[i])

        start = i
        i = freq[A[i]][-1]
        end = i

        for j in range(start, end):
            if A[j] not in cache:
                if freq[A[j]][-1] > i:
                    i = freq[A[j]][-1]

                cache.add(A[j])

        start = end
        end = i

        for j in range(start, end):
            if A[j] not in cache:
                if freq[A[j]][-1] > i:
                    i = freq[A[j]][-1]
                cache.add(A[j])

        i += 1

    print(pow(2, len(C) - 1, mod))


solve()
