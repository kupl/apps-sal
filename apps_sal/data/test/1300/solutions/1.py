from collections import defaultdict


def solve():
    (N, C) = map(int, input().split())
    arr = [int(k) for k in input().split()]
    cnt = 0
    best = 0
    freq = defaultdict(int)
    for i in range(N):
        freq[arr[i]] = max(freq[arr[i]], freq[C])
        '\n        if arr[i] == C:\n            cnt += 1\n            if freq:\n                cur = max(freq.values())\n                if cur > best:\n                    best = cur\n                \n                freq = defaultdict(int)\n            continue\n        '
        freq[arr[i]] += 1
        cur = freq[arr[i]] - freq[C]
        if cur > best:
            best = cur
    print(best + freq[C])


solve()
