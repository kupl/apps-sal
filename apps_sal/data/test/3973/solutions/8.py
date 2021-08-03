n, m = list(map(int, input().split()))
As = list(map(int, input().split()))


def solve(n, m, As):
    weighted_sum = [0] * m
    row_sum = [0] * m
    col_sum = [0] * m
    delta_sum = [0] * m
    delta_sum0 = 0
    delta_weighted = 0
    sol = 0
    As = [a - 1 for a in As]
    for i in range(n - 1):
        a = As[i]
        b = As[i + 1]
        sol += (b - a) % m
        if a == b or (a + 1) % m == b:
            continue
        row_sum[a] += 1
        col_sum[b] += 1
        weighted_sum[b] += (b - a - 1) % m
        if (a > b and a != m - 1):
            delta_sum0 += 1
            delta_weighted += m - a - 1
    delta_sum[0] = delta_sum0
    for i in range(1, m):
        delta_sum0 = delta_sum0 + row_sum[i - 2] - col_sum[i - 1]
        delta_sum[i] = delta_sum0
    record = delta_weighted
    for x in range(1, m):
        delta_weighted += delta_sum[x] - weighted_sum[x - 1]
        record = max(record, delta_weighted)
    return sol - record


print((solve(n, m, As)))
