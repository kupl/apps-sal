n = int(input())
a = list(map(int, input().split()))

b = [0 for i in range(n)]

cnt = 0
for i in range(n):
    if i - a[i] >= 0:
        cnt += b[i - a[i]]
    if i + a[i] < n:
        b[i + a[i]] += 1
print(cnt)
