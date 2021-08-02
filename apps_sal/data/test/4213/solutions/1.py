N = int(input())
data = list(map(int, input().split()))

max = 0
min = 1000000000

for i in range(len(data)):
    if max < data[i]:
        max = data[i]
    if min > data[i]:
        min = data[i]
print(max - min)
