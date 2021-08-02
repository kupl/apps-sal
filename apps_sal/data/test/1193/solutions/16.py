n, k = list(map(int, input().split()))
data = list(map(int, input().split()))
line = [0] * n
maxx = 0
for i in range(n):
    count = 0
    for j in range(n):
        if data[i] <= data[j]:
            count += 1
    line[i] = count
    if count >= k:
        maxx = max(maxx, data[i])
print(maxx)
