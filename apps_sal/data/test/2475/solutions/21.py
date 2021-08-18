N = int(input())
slist = list(map(int, input().split()))
ans = 0
for C in range(1, N - 1, 1):
    score = 0
    for k in range((N - 1) // C):
        if (k - 1) * C == N - 1 - k * C:
            break
        if 2 * k * C == N - 1:
            break
        score += slist[k * C] + slist[N - 1 - k * C]
        ans = max(ans, score)
print(ans)
