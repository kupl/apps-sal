n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = a[0]
num = 2
idx = 1
while num < n:
    if num + 1 == n:
        ans += a[idx]
        num += 1
    else:
        ans += a[idx] * 2
        num += 2
        idx += 1
print(ans)
