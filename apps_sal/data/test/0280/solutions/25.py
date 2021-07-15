import itertools
import bisect

N, M = [int(n) for n in input().split()]
W = [int(n) for n in input().split()]
bridges = [[int(n) for n in input().split()] for _ in range(M)] # [length_i, weight_i] 

# sort by weight
bridges.sort(key=lambda x: x[1])

limits = [v for l, v in bridges]
len_rm = list(itertools.accumulate([l for l, v in bridges], max)) # running maximum
# len_rm[i]: the maximum length of the bridges whose load limit <= limits[i]

ans = -1
if max(W) <= min(limits):
    ans = 1000000000 # larger than maximum possible solution (7 x 10^8)
    for W_perm in itertools.permutations(W):
        lengths = [0 for _ in range(N)]
        for i in range(N):
            w_ij = W_perm[i]
            for j in range(i+1, N):
                w_ij += W_perm[j] # w_ij: total weight between i and j (inclusive)
                idx = bisect.bisect_left(limits, w_ij)
                if idx == 0: # all bridge accepts w_ij
                    x_ij = 0
                else: # bridges[0] ... bridges[i-1] cannot accept w_ij
                    x_ij = len_rm[idx-1]
                lengths[j] = max(lengths[j], lengths[i] + x_ij)

                # skipping trivial edges
                # even without this if-block, we can get AC
                if idx == M:
                    break
            
        candidate = lengths[-1]
        ans = min(ans, candidate)

print(ans)

