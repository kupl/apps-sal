n, k = list(map(int, input().split()))
sizes = list(map(int, input().split()))


def solve(n, k, sizes):
    if k >= n:
        return max(sizes)
    head = sizes[:n - k]
    tail = sizes[n - k:]
    for i, h in enumerate(head[::-1]):
        tail[i] += h
    return max(tail)


print(solve(n, k, sizes))
