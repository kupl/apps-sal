n = int(input())
a = sorted(list(map(int, input().split())))

cnt = 0
i = 0
while i < n - 1:
    while a[i] >= a[i + 1]:
        a[i + 1] += 1
        cnt += 1
    i += 1
print(cnt)
