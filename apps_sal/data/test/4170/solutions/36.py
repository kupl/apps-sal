n = int(input())
h = list(map(int, input().split(" ")))
count = 0
temp = 0
for i in range(1, n):

    if h[i] <= h[i - 1]:
        temp += 1
    else:
        count = max(count, temp)
        temp = 0
print(max(temp, count))
