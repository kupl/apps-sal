n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
sum = 0
for i in range(n):
    if b[i] == 1 or a[i] + a[i] < b[i]:
        sum = sum - 1
    else:
        sum = sum + (b[i] // 2) * (b[i] - b[i] // 2)
print(sum)
