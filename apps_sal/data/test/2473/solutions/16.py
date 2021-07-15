N, K = list(map(int, input().split()))
p_list = [[0] * 2 for i in range(N)]
for i in range(N):
    x, y = list(map(int, input().split()))
    p_list[i] = [x, y]

p_list.sort()
ans = float('inf')
for i in range(N - K + 1):
    for j in range(i + K - 1, N):
        x = abs(p_list[j][0] - p_list[i][0])
        y_list = []
        for k in range(i, j + 1):
            y_list.append((p_list[k][1]))
        y_list.sort()
        for k in range(len(y_list) - K + 1):
            ans = min(ans, x * abs(y_list[k + K - 1] - y_list[k]))

print(ans)

