arr = list(map(int, input().split()))
ans = 0
for i in range(len(arr)):
    pol = arr[i] // 14
    os = arr[i] % 14
    cur = 0
    if pol % 2 == 0:
        cur += pol
    j = i + 1
    if j == 14:
        j = 0
    for u in range(13):
        num = 0
        if u < os:
            num += 1
        num += arr[j] + pol
        if num % 2 == 0:
            cur += num
        j = j + 1
        if j == 14:
            j = 0
    if cur > ans:
        ans = cur
print(ans)
