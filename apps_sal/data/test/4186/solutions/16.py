n = int(input())
a = sorted(list(map(int, input().split())))
cnt = 0
for i in range(0, n, 2):
    cnt += a[i + 1] - a[i]
print(cnt)
