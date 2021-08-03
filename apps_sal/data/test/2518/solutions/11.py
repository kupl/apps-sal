n, a, b = list(map(int, input().split()))
h = [int(input())for _ in range(n)]
h.sort(reverse=True)
l = -1
r = 10**9
while r - l > 1:
    mid = (l + r) // 2
    cnt = 0
    for i in range(n):
        if h[i] - b * mid <= 0:
            break
        else:
            cnt += (h[i] - b * mid - 1) // (a - b) + 1
    if cnt > mid:
        l = mid
    else:
        r = mid
print(r)
