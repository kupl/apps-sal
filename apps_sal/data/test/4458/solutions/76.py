N = int(input())
P = list(map(int, input().split()))

ans = 1

p = P[0]

for i in range(N):
    if p > P[i]:
        ans = ans + 1
        p = P[i]


print(ans)
