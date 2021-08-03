N = int(input())
l = [0] * N
r = [0] * N
for i in range(N):
    l[i], r[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += r[i] - (l[i] - 1)
print(ans)
