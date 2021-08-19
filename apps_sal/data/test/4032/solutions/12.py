(n, k) = list(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))
cnt = 0
for i in range(n):
    if arr[i] > k:
        cnt = 1
        break
if cnt == 0:
    print(n)
else:
    cnt = i
    for i in range(n - 1, i - 1, -1):
        if arr[i] > k:
            break
        cnt += 1
    print(cnt)
