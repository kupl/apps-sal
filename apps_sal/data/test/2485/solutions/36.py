import itertools
H, W, N = [int(s) for s in input().split()]
hls = [0 for _ in range(H + 1)]
wls = [0 for _ in range(W + 1)]
bombs = [set() for _ in range(H + 1)]
for _ in range(N):
    h, w = [int(s) for s in input().split()]
    hls[h] += 1
    wls[w] += 1
    bombs[h].add(w)
hmax = max(hls)
wmax = max(wls)
hmaxls = [i for i in range(H + 1) if hls[i] == hmax]
wmaxls = [i for i in range(W + 1) if wls[i] == wmax]
for h, w in itertools.product(hmaxls, wmaxls):
    if not(w in bombs[h]):
        print(hmax + wmax)
        return
else:
    print(hmax + wmax - 1)
