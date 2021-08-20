n = int(input())
a = list(map(int, input().split()))
a.sort()
m = a[1] - a[0]
cnt = 0
for i in range(1, len(a)):
    if a[i] - a[i - 1] == m:
        cnt += 1
    elif a[i] - a[i - 1] < m:
        m = a[i] - a[i - 1]
        cnt = 1
ans = str(m) + ' ' + str(cnt)
print(ans)
