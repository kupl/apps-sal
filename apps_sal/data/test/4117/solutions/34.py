def cin():
    return list(map(int, input().split()))


N = int(input())
L = cin()
count = 0

for i in range(0, N - 2):
    for j in range(1 + i, N - 1, 1):
        for k in range(1 + j, N, 1):
            data = [L[i], L[j], L[k]]
            data.sort()
            if data[0] == data[1] or data[1] == data[2] or data[2] == data[0]:
                continue
            if data[0] + data[1] > data[2]:
                count += 1

print(count)
