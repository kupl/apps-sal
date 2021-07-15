n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for left in range(n + 1):
    for right in range(n + 1):
        if left == 0 and right == 0:
            continue
        rest = k - left - right
        if left + right > n or rest < 0:
            break
        arr = v[:left] + v[n - right:]
        minus = 0
        neg = [x for x in arr if x < 0]
        if len(neg) > 0:
            neg.sort()
            minus = sum(neg[:rest])
        ans = max(ans, sum(arr) - minus)

print(ans)
