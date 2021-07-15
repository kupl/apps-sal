N = map(int, input().split())
point = list(map(int,input().split()))

max = 0
min = 1000

for i in range(len(point)):
    if max < point[i]:
        max = point[i]
    if min > point[i]:
        min = point[i]
print(max - min)
