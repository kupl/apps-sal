n = int(input())
a = list(map(int, input().split()))
cnt = 0
a.sort(reverse=True)
for i in range(n):
    if i % 2 == 0:
        cnt += a[i]
    else:
        cnt -= a[i]
print(cnt)
