n = int(input())
data = list(map(int,input().split()))
point = 0
i = 1
while i <= len(data) - 2:
    if data[i-1] < data[i] and data[i] < data[i+1]:
        point += 1
    if data[i - 1] > data[i] and data[i] > data[i + 1]:
        point += 1
    i += 1

print(point)
