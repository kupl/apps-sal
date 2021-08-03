n = int(input())
a = list(map(int, input().split()))
t = int(input())
a.sort()
m = 1
count = 0
for i in range(n):
    for j in range(i, n):
        if (a[j] - a[i] <= t):
            count += 1
    m = max(count, m)
    count = 0
print(m)
