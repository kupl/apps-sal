N = int(input())
P = list(map(int, input().split()))

ans = 0

if P[-1] == N:
    ans += 1
    P[-1] = -1
    if P[-2] == N - 1:
        P[-2] = -1

for i in range(N - 1):
    if P[i] == i + 1:
        ans += 1
        if P[i + 1] == i + 2:
            P[i + 1] = -1

print(ans)
