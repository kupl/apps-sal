n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = max(a)
tmp = a[0]
cnt = 0
for i in range(1, n):
    if tmp < a[i]:
        tmp = a[i]
        cnt = 1
    else:
        cnt += 1
    if cnt == k:
        ans = tmp
        break
print(ans)

