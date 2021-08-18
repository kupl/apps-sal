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
    w2x = dict()
    for F in itertools.product([0, 1], repeat=N):
        w = sum([w for w, f in zip(W, F) if f == 1])
        if w in w2x:
            continue
        idx = bisect.bisect_left(limits, w)
        w2x[w] = 0 if idx == 0 else len_rm[idx - 1]

    ans = 1000000000
    for W_perm in itertools.permutations(W):
        lengths = [0 for _ in range(N)]
        for i in range(N):
            w_ij = W_perm[i]
            for j in range(i + 1, N):
                w_ij += W_perm[j]
                lengths[j] = max(lengths[j], lengths[i] + w2x[w_ij])

                if w_ij > limits[-1]:
                    break

        candidate = lengths[-1]
        ans = min(ans, candidate)

print(ans)
