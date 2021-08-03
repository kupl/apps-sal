from collections import Counter
N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]
ctr = Counter()
pairs = {}
starts = set()
ends = set()
free = 0
for a, b in AB:
    if a > 0 and b > 0:
        pairs[a] = b
        ctr[a] += 1
        ctr[b] += 1
    elif a > 0:
        ctr[a] += 1
        starts.add(a)
    elif b > 0:
        ctr[b] += 1
        ends.add(b)
    else:
        free += 1

if any(v > 1 for v in ctr.values()):
    print('No')
    return

dp = [False] * (N + 1)
dp[0] = True
for i in range(N):
    if not dp[i]:
        continue
    for j in range(i + 1, N + 1):
        if dp[j]:
            continue
        l = j - i
        for s in range(2 * i + 1, 2 * i + l + 1):
            t = s + l
            if s in pairs:
                if pairs[s] != t:
                    break
            if s in starts and t in ends:
                break
            if s in ends:
                break
            if t in starts:
                break
        else:
            dp[j] = True
print('Yes' if dp[-1] else 'No')
