n = int(input())
data = [input().split() for i in range(n)]
for i in range(n):
    data[i].append(i + 1)
    if 10 <= int(data[i][1]) < 100:
        data[i][1] = '0' + str(data[i][1])
    elif int(data[i][1]) < 10:
        data[i][1] = '00' + str(data[i][1])
data.sort(key=lambda x: x[1], reverse=True)
data.sort(key=lambda x: x[0])
for i in range(n):
    print(data[i][2])
