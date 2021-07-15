n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
ans = 0
p = 1
i = 0
while n != 0:
    tp = arr[i]
    ans += 2 * (tp - p) * (round(n / k + 0.49999999999999))
    while n != 0 and arr[i] == tp:
        n -= 1
        i += 1
    p = tp
print(ans)


