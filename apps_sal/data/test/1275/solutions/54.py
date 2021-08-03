N, K = map(int, input().split())
alpha = 2
sum = 0
while alpha <= 2 * N:
    beta = alpha - K
    if 2 <= beta and beta <= 2 * N:
        if alpha <= N + 1:
            if beta <= N + 1:
                sum += (alpha - 1) * (beta - 1)
            else:
                sum += (alpha - 1) * (2 * N - beta + 1)
        else:
            if beta <= N + 1:
                sum += (2 * N - alpha + 1) * (beta - 1)
            else:
                sum += (2 * N - alpha + 1) * (2 * N - beta + 1)
    alpha += 1
print(sum)
