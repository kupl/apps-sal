n = int(input())
a = [int(num) for num in input().split()]
count = 0
for i in range(1, n-1):
    if a[i-1] < a[i] and a[i] < a[i+1]:
        count += 1
    elif a[i-1] > a[i] and a[i] > a[i+1]:
        count += 1
print(count)

