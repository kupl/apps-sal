(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s = 0
start = 0
for i in range(n):
    s += a[i]
    if s >= k:
        ans += n - i
        for j in range(start, i + 1):
            s -= a[j]
            if s >= k:
                ans += n - i
            else:
                start = j + 1
                break
print(ans)
