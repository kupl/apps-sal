n = int(input())
stations = []
for i in range(n - 1):
    stations.append(list(map(int, input().split())))
ans = [0]
time_matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i + 1):
        if i < n - 1:
            if time_matrix[i][j] % stations[i][2] == 0:
                waiting = 0
            else:
                waiting = stations[i][2] - time_matrix[i][j] % stations[i][2]
            time_matrix[i + 1][j] = max(time_matrix[i][j] + stations[i][0] + waiting, stations[i][0] + stations[i][1])
for i in range(n):
    print(time_matrix[n - 1][i])
