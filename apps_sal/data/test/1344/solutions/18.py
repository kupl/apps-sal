n = int(input())
a = list(map(int, input().split()))
count = 1
max_count = 1
for i in range(1, n):
    if a[i] > a[i - 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
