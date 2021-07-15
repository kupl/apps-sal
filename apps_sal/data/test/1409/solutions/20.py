n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] + k <= 5:
        cnt += 1
print(cnt // 3)
