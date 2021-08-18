n = int(input())

arr = list(map(int, input().split()))

memo = [-1 for i in range(n + 1)]


def can_win(idx):
    if memo[idx] != -1:
        return memo[idx]
    res = False

    delta = arr[idx]
    nidx = idx + delta
    while nidx < n:
        if arr[nidx] > arr[idx] and not can_win(nidx):
            res = True
            break
        nidx += delta

    nidx = idx - delta
    while not res and nidx >= 0:
        if arr[nidx] > arr[idx] and not can_win(nidx):
            res = True
            break
        nidx -= delta

    memo[idx] = res
    return res


ans = ['A' if can_win(i) else 'B' for i in range(n)]
print(''.join(ans))
