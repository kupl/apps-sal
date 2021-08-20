(N, M) = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(M)]
data = sorted(data, key=lambda x: x[1])
count = 1
left = data[0][1]
for i in range(1, M):
    if data[i][0] < left:
        left = max(data[i][0], left)
    else:
        count += 1
        left = data[i][1]
print(count)
