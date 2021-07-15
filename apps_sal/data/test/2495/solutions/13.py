n = int(input())
a = list(map(int, input().split()))

flag = 1
temp_1 = 0
temp = 0
for i in range(n):
    temp += a[i]
    if flag * temp <= 0:
        temp_1 += 1 - flag * temp
        temp = flag
    flag *= -1

flag = -1
temp_2 = 0
temp = 0
for i in range(n):
    temp += a[i]
    if flag * temp <= 0:
        temp_2 += 1 - flag * temp
        temp = flag
    flag *= -1

print(min(temp_1, temp_2))
