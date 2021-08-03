N = int(input())
a = list(map(int, input().split()))

cum = [0]
for i in range(N):
    cum.append(cum[-1] + a[i])

ans = 10**20
for i in range(1, N):
    tmp = abs(cum[-1] - cum[i] - cum[i])
    ans = min(ans, tmp)

print(ans)
