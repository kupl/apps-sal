import itertools
import bisect

N, M = [int(n) for n in input().split()]
W = [int(n) for n in input().split()]
bridges = [[int(n) for n in input().split()] for _ in range(M)]

bridges.sort(key=lambda x: x[1])

limits = [v for l, v in bridges]
len_rm = list(itertools.accumulate([l for l, v in bridges], max))

ans = -1
if max(W) <= min(limits):
    ans = 1000000000
    for W_perm in itertools.permutations(W):
        lengths = [0 for _ in range(N)]
        for i in range(N):
            w_ij = W_perm[i]
            for j in range(i + 1, N):
                w_ij += W_perm[j]
                idx = bisect.bisect_left(limits, w_ij)
                if idx == 0:
                    x_ij = 0
                else:
                    x_ij = len_rm[idx - 1]
                lengths[j] = max(lengths[j], lengths[i] + x_ij)

                if idx == M:
                    break

        candidate = lengths[-1]
        ans = min(ans, candidate)

print(ans)
