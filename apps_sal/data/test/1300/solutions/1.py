from collections import defaultdict


def solve():
    N, C = map(int, input().split())

    arr = [int(k) for k in input().split()]

    cnt = 0
    best = 0
    freq = defaultdict(int)

    for i in range(N):
        freq[arr[i]] = max(freq[arr[i]], freq[C])
        '''
        if arr[i] == C:
            cnt += 1
            if freq:
                cur = max(freq.values())
                if cur > best:
                    best = cur
                
                freq = defaultdict(int)
            continue
        '''
        freq[arr[i]] += 1
        cur = freq[arr[i]] - freq[C]
        if cur > best:
            best = cur

    print(best + freq[C])


solve()
