info_data = int(input())
data = []
for i in range(info_data):
    data.append(list(map(int, input().split())))
data.sort()
result = data[0][1]
for i in range(info_data):
    if result > data[i][1]:
        result = data[i][0]
    else:
        result = data[i][1]
print(result)
