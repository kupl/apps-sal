(A, B, X) = list(map(int, input().split()))
left = 0
right = 1000000001
while right - left > 1:
    mid = (left + right) // 2
    if A * mid + B * len(str(mid)) > X:
        right = mid
    else:
        left = mid
print(left)
