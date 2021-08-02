import array

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
tmp = A[0]
right = 0


for i in range(N):
    for j in range(right + 1, N):
        if tmp >= K:
            break
        tmp += A[j]

        right += 1

    if tmp >= K:
        ans += N - right
        if N - right == 0:
            break

    tmp -= A[i]
print(ans)
