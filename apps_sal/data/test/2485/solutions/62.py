
H, W, M = list(map(int, input().split()))

HSum = [0 for _ in range(H)]
WSum = [0 for _ in range(W)]


bombs = set()
for _ in range(M):
    hi, wi = [int(x) - 1 for x in input().split()]
    HSum[hi] += 1
    WSum[wi] += 1
    bombs.add((hi, wi))


curMax = 0


hMax = max(HSum)
wMax = max(WSum)
tmpMax = hMax + wMax

ans = 0

hSumMaxOnly = [h for h, x in enumerate(HSum) if x == hMax]
wSumMaxOnly = [w for w, y in enumerate(WSum) if y == wMax]

for h in hSumMaxOnly:
    if ans == tmpMax:
        break
    for w in wSumMaxOnly:
        if (h, w) in bombs:
            ans = tmpMax - 1
        else:
            ans = tmpMax
            break


print(ans)
