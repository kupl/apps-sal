n, k = map(int, input().split())
a = list(map(int, input().split()))
k = 5 - k
cnt = 0
for i in range(n):
    if a[i] <= k:
        cnt += 1
print(cnt // 3)
