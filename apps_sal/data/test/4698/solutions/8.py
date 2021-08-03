n = int(input())
data_1 = list(map(int, input().split()))
m = int(input())
data_2 = [input().split() for i in range(m)]


for i in range(m):
    sum = 0
    b = int(data_2[i][0]) - 1
    a = data_1[b]
    data_1[b] = int(data_2[i][1])
    for j in range(n):
        sum += data_1[j]
    print(sum)
    data_1[b] = a
