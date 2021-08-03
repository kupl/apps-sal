n = int(input())
A = list(map(int, input().split()))

cumsum_A = []
cumsum = 0
for a in A:
    cumsum += a
    cumsum_A.append(cumsum)

ans = float('INF')
left = 0
right = 2

for center in range(1, n - 2):
    ll_value = cumsum_A[left]
    lc_value = cumsum_A[center] - ll_value
    cr_value = cumsum_A[right] - cumsum_A[center]
    rr_value = cumsum_A[-1] - cumsum_A[right]

    while abs(ll_value - lc_value) > abs(ll_value - lc_value + 2 * A[left + 1]):
        if left == center - 1:
            break
        left += 1
        ll_value += A[left]
        lc_value -= A[left]

    while abs(cr_value - rr_value) > abs(cr_value - rr_value + 2 * A[right + 1]):
        if right == n - 2:
            break
        right += 1
        cr_value += A[right]
        rr_value -= A[right]

    candidate = max(ll_value, lc_value, cr_value, rr_value) - min(ll_value, lc_value, cr_value, rr_value)
    ans = min(ans, candidate)

print(ans)
