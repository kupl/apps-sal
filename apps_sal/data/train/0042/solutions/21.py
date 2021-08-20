from math import log2
from math import ceil
for _ in range(int(input())):
    S = list(map(int, list(input())))
    combs = 0
    maxlen = ceil(log2(len(S)))
    prezeros = 0
    next1 = [0] * len(S)
    nxt = len(S) - 1
    for i in range(len(S) - 1, -1, -1):
        if S[i] == 1:
            nxt = i
        next1[i] = nxt
    for l in range(len(S)):
        if S[l] == 0:
            nxtl = next1[l]
            val = 0
            lcomb = 0
            for r in range(nxtl, min(nxtl + maxlen + 1, len(S))):
                val = 2 * val + S[r]
                if val == r - l + 1:
                    lcomb += 1
            combs += lcomb
            continue
        val = 0
        lcomb = 0
        for r in range(l, min(l + maxlen + 1, len(S))):
            val = 2 * val + S[r]
            if val == r - l + 1:
                lcomb += 1
        combs += lcomb
        prezeros = 0
    print(combs)
