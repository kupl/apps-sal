N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(N):
    tako1 = D[i]

    for j in range(0, i):
        tako2 = D[j]

        ans += tako1 * tako2

    for j in range(i + 1, N):
        tako2 = D[j]

        ans += tako1 * tako2

print(ans // 2)
