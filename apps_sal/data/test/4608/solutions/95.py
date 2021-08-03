n = int(input())
data = [int(input()) for i in range(n)]
count = 0
temp = 1
for i in range(n):
    temp = data[temp - 1]
    count += 1
    if temp == 2:
        print(count)
        break
else:
    print(-1)
