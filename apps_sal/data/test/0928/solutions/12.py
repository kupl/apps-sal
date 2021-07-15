N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()] + [0]

cnt = 0
left = 0
right = 0
t = A[right]
while right < N:
    if t >= K:
        cnt += N - right
    if t >= K and left < right:
        t -= A[left]
        left += 1
    elif t >= K and left == right:
        left += 1
        right += 1
        t = A[right]
    else:
        right += 1
        t += A[right]
print(cnt)

