def construct(is_reversed=False):
    start, end, step = 0, N - 1, 1
    if is_reversed:
        start, end, step = N - 1, 0, -1
    ret = []
    for i in range(start, end, step):
        ret.append((i + 1, i + step + 1))
    return ret


def solve():
    max_A = max(A)
    min_A = min(A)
    if max_A == min_A:
        return []
    elif abs(max_A) >= abs(min_A):
        idx = A.index(max_A)
        return [(idx + 1, i + 1) for i in range(N) if i != idx] + construct()
    elif abs(max_A) < abs(min_A):
        idx = A.index(min_A)
        return [(idx + 1, i + 1) for i in range(N) if i != idx] + construct(True)


N = int(input())
A = list(map(int, input().split()))
ans = solve()
print((len(ans)))
for e in ans:
    print((*e))

