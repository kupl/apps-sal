n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
sum_a = [0] * (n + 1)
for i in range(1, n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]
sum_a.append(10 ** 11)
def is_ok(mid, now):
    nonlocal k, n, sum_a
    if sum_a[mid] - sum_a[now] >= k:
        return True
    else:
        return False
ans = 0
for i in range(n):
    top = n + 1
    bottom = i
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if is_ok(mid, i):
            top = mid
        else:
            bottom = mid
    ans += n + 1 - top
print(ans) 
