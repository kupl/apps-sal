import itertools
import bisect

N, M = [int(n) for n in input().split()]
W = [int(n) for n in input().split()]
bridges = [[int(n) for n in input().split()] for _ in range(M)] # [length_i, load_limit_i] 

# sort by load limit
bridges.sort(key=lambda x: x[1])

limits = [v for l, v in bridges]
len_rm = list(itertools.accumulate([l for l, v in bridges], max)) # running maximum
# len_rm[i]: the maximum length of the bridges whose load limit <= limits[i]

ans = -1
if max(W) <= min(limits):
    # precompute mapping
    # from: (sum of) weights, (w)
    # to: maximum part length (x) whose load limit <= w
    w2x = dict()
    for F in itertools.product([0, 1], repeat=N):
        w = sum([w for w, f in zip(W, F) if f == 1])
        if w in w2x:
            continue        
        idx = bisect.bisect_left(limits, w)
        w2x[w] = 0 if idx == 0 else len_rm[idx-1]
    
    ans = 1000000000 # larger than maximum possible solution (7 x 10^8)
    for W_perm in itertools.permutations(W):
        lengths = [0 for _ in range(N)]
        for i in range(N):
            w_ij = W_perm[i]
            for j in range(i+1, N):
                w_ij += W_perm[j] # w_ij: total weight between i and j (inclusive)
                lengths[j] = max(lengths[j], lengths[i] + w2x[w_ij])

                # skipping trivial edges
                # even without this if-block, we can get AC
                if w_ij > limits[-1]:
                    break
            
        candidate = lengths[-1]
        ans = min(ans, candidate)

print(ans)

