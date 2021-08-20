N = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i == N - 1:
        if P[i] == i + 1:
            ans += 1
        break
    (a, b) = (P[i], P[i + 1])
    if a == i + 1:
        ans += 1
        P[i] = b
        P[i + 1] = a
print(ans)
