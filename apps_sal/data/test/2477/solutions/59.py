(N, K) = map(int, input().split())
A = list(map(int, input().split()))
r = max(A)
l = 0
while l + 1 < r:
    mid = (l + r) // 2
    cnt = 0
    for a in A:
        if a > mid:
            if a % mid == 0:
                cnt += a // mid - 1
            else:
                cnt += a // mid
    if cnt > K:
        l = mid
    else:
        r = mid
print(r)
