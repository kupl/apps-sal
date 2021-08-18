N = int(input())
A = list(map(int, input().split()))

cul_sum = [0 for _ in range(N + 1)]
for i in range(N):
    cul_sum[i + 1] = A[i] + cul_sum[i]


def diff_left(center, left):
    return abs(cul_sum[center + 1] - 2 * cul_sum[left + 1])


def diff_right(center, right):
    return abs(cul_sum[N] - 2 * cul_sum[right + 1] + cul_sum[center + 1])


L = [-1 for _ in range(N - 1)]
R = [-1 for _ in range(N - 1)]
l = 0
r = 2
ans = float('inf')
for i in range(1, N - 2):
    while l < i and diff_left(i, l) > diff_left(i, l + 1):
        l += 1
    if r <= i:
        r = i + 1
    while r < N and diff_right(i, r) > diff_right(i, r + 1):
        r += 1
    part_sum = [
        cul_sum[l + 1],
        cul_sum[i + 1] - cul_sum[l + 1],
        cul_sum[r + 1] - cul_sum[i + 1],
        cul_sum[N] - cul_sum[r + 1],
    ]
    ans = min(ans, max(part_sum) - min(part_sum))

print(ans)
