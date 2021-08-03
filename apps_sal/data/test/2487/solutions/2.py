N = int(input())
l = [list(map(int, input().split())) for l in range(N - 1)]
c = 0
for i in range(N - 1):
    c += min(l[i]) * (N + 1 - max(l[i]))
print(N * (N + 1) * (N + 2) // 6 - c)
