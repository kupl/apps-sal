N = int(input())
a = [int(input()) for i in range(N)]

count = [0] * (N)

i = 1
min_num = 0
count[i - 1] += 1
while True:
    i = a[i - 1]
    min_num += 1
    if i == 2:
        print(min_num)
        return
    if count[i - 1] == 0:
        count[i - 1] += 1
    else:
        break

print(-1)
