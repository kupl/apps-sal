n = int(input())
a = list(map(int, input().split()))
minimum = min(a)
max_segment = 0
count = 0
a = a + a
for i in range(len(a)):
    if a[i] == minimum:
        max_segment = max(count, max_segment)
        count = 0
    else:
        count += 1
max_segment = max(count, max_segment)
print(minimum * n + max_segment)
