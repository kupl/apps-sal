n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
for i in range(len(a)):
    if a[i] + k <= 5:
        sum += 1
print(sum // 3)
