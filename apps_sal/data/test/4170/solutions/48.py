N = int(input())
H = list(map(int, input().split(' ')))
count = 0
maxCount = 0
for i in range(len(H) - 1):
    if H[i] >= H[i + 1]:
        count = count + 1
    else:
        if maxCount <= count:
            maxCount = count
        count = 0
print(max(count, maxCount))
