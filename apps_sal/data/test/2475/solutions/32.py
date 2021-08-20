N = int(input())
ss = list(map(int, input().split()))
ans = 0
for C in range(1, N):
    score = 0
    for k in range(1, (N - 1) // C + 1):
        if (N - 1) % C == 0 and k * C >= N - 1 - k * C:
            break
        if N - 1 - k * C <= C:
            break
        score += ss[k * C] + ss[N - 1 - k * C]
        ans = max(ans, score)
print(ans)
