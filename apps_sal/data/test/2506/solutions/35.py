(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)
acum = [arr[0]]
for i in range(1, n):
    acum.append(acum[-1] + arr[i])
l = 0
r = 2 * 10 ** 5 + 1
while r - l != 1:
    mid = (l + r) // 2
    tmp = 0
    cnt = 0
    pos = n - 1
    for i in range(n):
        while pos != -1:
            if arr[i] + arr[pos] >= mid:
                cnt += pos + 1
                tmp += arr[i] * (pos + 1) + acum[pos]
                break
            else:
                pos -= 1
                if pos == -1:
                    break
    if cnt <= m:
        r = mid
    else:
        l = mid
tmp += (m - cnt) * l
print(tmp)
