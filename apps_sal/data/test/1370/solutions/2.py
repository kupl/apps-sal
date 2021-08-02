import sys
from itertools import product

read = sys.stdin.read
readline = sys.stdin.readline

H, W, K = list(map(int, readline().split()))
S = [list(map(int, list(readline().rstrip()))) for _ in range(H)]

answer = 10 ** 10
for i in product((0, 1), repeat=H - 1):
    cnt = sum(i)
    if cnt >= answer:
        continue
    cuts = []
    cuts.append(S[0].copy())
    for j in range(H - 1):
        if i[j] == 1:
            cuts.append(S[j + 1].copy())
        else:
            tmp1 = cuts[-1]
            tmp2 = S[j + 1]
            for k in range(W):
                tmp1[k] += tmp2[k]
    for j in cuts:
        if any(k > K for k in j):
            break
    else:
        h = len(cuts)
        tmp = [0] * h

        for j in range(W):
            for k in range(h):
                tmp[k] += cuts[k][j]
            for k in tmp:
                if k > K:
                    cnt += 1
                    tmp = [cuts[l][j] for l in range(h)]
                    break
        if cnt < answer:
            answer = cnt

print(answer)
