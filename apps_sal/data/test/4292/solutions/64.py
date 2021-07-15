n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range(k):
    count += a[i]

print(count)
