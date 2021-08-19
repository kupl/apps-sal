from collections import deque
import heapq


def solve(N, K, Vi):
    ans = 0
    for ab in range(min(N, K) + 1):
        for a in range(ab + 1):
            b = ab - a
            have = Vi[:a] + Vi[N - b:]
            have.sort()
            s = sum(have)
            for i in range(K - ab):
                if len(have) <= i:
                    break
                elif have[i] < 0:
                    s += abs(have[i])
                else:
                    break
            ans = max(ans, s)
    print(ans)


def __starting_point():
    (N, K) = list(map(int, input().split()))
    Vi = [int(i) for i in input().split()]
    solve(N, K, Vi)


__starting_point()
