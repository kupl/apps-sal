from itertools import accumulate

# 入力
H, W, K = map(int, input().split())
S = [list(map(int, list(input()))) for _ in range(H)]

# 転置 + 行ごと(つまり列ごと)の白チョコの数を数えている
accs = [[0]+list(accumulate(l)) for l in zip(*S)]

ans = float('inf')

for i in range(1 << H - 1):
    parts = []
    cuts = 0
    for k in range(H - 1):
        if i & (1 << k):
            cuts += 1
            parts.append(k+1)
    
    parts.append(H)
    cts = [0]*len(parts)
    for j in range(W):
        prev = 0
        flag1 = False
        for idx, p in enumerate(parts):
            c = accs[j][p] - accs[j][prev]
            cts[idx] += c
            if cts[idx] > K:
                flag1 = True
                break
            prev = p
        if flag1:
            cuts += 1
            prev = 0
            flag2 = False
            for idx, p in enumerate(parts):
                c = accs[j][p] - accs[j][prev]
                if c > K:
                    flag2 = True
                    break
                cts[idx] = c
                prev = p
            if flag2:
                break
    else:
        ans = ans if ans < cuts else cuts

print(ans)
