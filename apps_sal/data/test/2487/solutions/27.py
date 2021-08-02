N = int(input())
l = [sorted(list(map(int, input().split()))) for l in range(N - 1)]
c = 0
for i in range(N - 1): c += l[i][0] * (N + 1 - l[i][1])
print(N * (N + 1) * (N + 2) // 6 - c)
