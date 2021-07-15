n = int(input())
a = list(map(int, list(input().strip())))
cnt = 0
now = 1
for i in range(n):
    if now:
        cnt += 1
        now = a[i] % 2
        a[i] += 1
        a[i] %= 2
print(cnt)
