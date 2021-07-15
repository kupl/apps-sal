def min_sub_array(day, k):
    if not day:
        return [0] * (k + 1)
    n = len(day)
    best = [float('inf')] * (n + 1)
    best[0] = 0
    best[1] = 1
    for size in range(2, n + 1):
        for i in range(n + 1 - size):
            best[size] = min(best[size], day[i + size - 1] - day[i] + 1)
    output = [0] * (k + 1)
    for i in range(k + 1):
        if n - i > 0:
            output[i] = best[n - i]
    return output


N, M, K = list(map(int, input().split()))

day = [i for i, val in enumerate(input()) if val == '1']
best = min_sub_array(day, K)

for _ in range(N - 1):
    day = [i for i, val in enumerate(input()) if val == '1']
    new_day_best = min_sub_array(day, K)

    new_best = [float('inf')] * (K + 1)
    for i in range(K + 1):
        for j in range(i + 1):
            new_best[i] = min(new_best[i], new_day_best[j] + best[i - j])
    best = new_best
print(best[K])

