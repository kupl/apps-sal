N, K = map(int, input().split())

Alist = list(map(int, input().split()))

left = 0
right = max(Alist)

while right - left > 1:
    mid = (left + right) // 2
    
    cnt = 0
    for A in Alist:
        if A % mid == 0:
            cnt += (A // mid) - 1
        else:
            cnt += (A // mid)
    
    if cnt <= K:
        right = mid
    else:
        left = mid

print(right)
